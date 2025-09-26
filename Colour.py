"""Your task is to implement a class that accepts a color palette designation in HEX format as a string and can convert it to RGB format using the properties red, green, and blue.
For this task, write only the implementation of the Colour class."""

class Colour:
    def __init__(self, colour):
        self.colour = colour

    @property
    def red(self):
        return int(self.colour[1:3], 16)

    @property
    def green(self):
        return int(self.colour[3:5], 16)

    @property
    def blue(self):
        return int(self.colour[5:7], 16)


test_colour = Colour("#00ff2d")
print(test_colour.red)
print(test_colour.green)
print(test_colour.blue)