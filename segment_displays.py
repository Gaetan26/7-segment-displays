from machine import Pin
import utime


letters = {
    'A' : [0, 1, 2, 4, 5, 6],
    'b' : [2, 3, 4, 5, 6],
    'C' : [0, 5, 4, 3],
    'd' : [1, 2, 3, 4, 6],
    'E' : [0, 6, 5, 4, 3],
    'F' : [0, 5, 4, 6],
    'H' : [6, 5, 4, 2, 1],
    'L' : [5, 4, 3]
}


class SegmentDisplays:

    def __init__(self, a, b, c, d, e, f, g, dp):
        self.pins = [
            Pin(a, Pin.OUT), 
            Pin(b, Pin.OUT), 
            Pin(c, Pin.OUT), 
            Pin(d, Pin.OUT), 
            Pin(e, Pin.OUT), 
            Pin(f, Pin.OUT), 
            Pin(g, Pin.OUT), 
            Pin(dp, Pin.OUT)
        ]

        self.clear()


    def turn_on(self, *args):
        for i in args:
            if isinstance(i, list):
                for j in i:
                    self.pins[j].value(1)
            else:
                self.pins[i].value(1)


    def clear(self):
        for pin in self.pins:
            pin.value(0)    


    def range(self, start=0, end=9, step=1, sleep=1000):
        for number in range(start, end+1, step):
            self.print(number=number)
            utime.sleep_ms(sleep)
    

    def range_letters(self, sleep=1000):
        for letter in [ 'A', 'b', 'C', 'd', 'E', 'F', 'H', 'L' ]:
            self.print(letter=letter)
            utime.sleep_ms(sleep)

    def print(self, number=None, letter=None, point=False):
        self.clear()
        
        if point:
            self.turn_on(7)
            
        if letter is not None:
            if letter in list(letters.keys()):
                self.turn_on(letters[letter])
            return True
        
        if number == 0:
            self.turn_on(0, 1, 2, 3, 4, 5)
            return True
        
        elif number == 1:
            self.turn_on(1, 2)
            return True
        
        elif number == 2:
            self.turn_on(0, 1, 6, 4, 3)
            return True
        
        elif number == 3:
            self.turn_on(0, 1, 2, 3, 6)
            return True
        
        elif number == 4:
            self.turn_on(5, 6, 1, 2)
            return True
        
        elif number == 5:
            self.turn_on(0, 5, 6, 2, 3)
            return True
        
        elif number == 6:
            self.turn_on(0, 2, 3, 4, 5, 6)
            return True
        
        elif number == 7:
            self.turn_on(0, 1, 2)
            return True
        
        elif number == 8:
            self.turn_on(0, 1, 2, 3, 4, 5, 6)
            return True
        
        elif number == 9:
            self.turn_on(0, 1, 2, 3, 5, 6)
            return True