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
    def __init__(self, start):
        """Creates a start point to modify and reset point"""
        self.s = start
        self.r = start
    def generate(self):
        """Prints the value and adds one to it"""
        print(t.s)
        self.s+=1
    def reset(self):
        """Resets the value to the original input"""
        self.s = self.r

t = SerialGenerator(start=10)
t.generate()
t.generate()
t.generate()
t.reset()
t.generate()