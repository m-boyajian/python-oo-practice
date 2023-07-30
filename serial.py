"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """Serial generator class is defined & takes optional argument 'start.' If no value is provided for 'start' it resorts to 0. 
    Init constructor initializes the class. Sets the start attribute to the given start value & initializes 'next_num'
    to the same value as starting #."""
    def __init__(self, start=0):
        self.start = start
        self.next_num = start
    """Genrate method generates the next sequential #. It stores the current value of next_num in current_num & then increments 
    next_num by 1 for the next call."""
    def generate(self):
        current_num = self.next_num
        self.next_num += 1
        return current_num
    def reset(self):
        self.next_num = self.start
    
"""Springboard's solution:
    def __init__(self, start=0):
        Make a new generator, starting at start.
    self.start = self.next = start
        Show representation.
    def __repr__(self):
        Return next serial.
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        
        self.next += 1
        return self.next - 1

    def reset(self):
        Reset number to original start.
        self.next = self.start"""
          
    


