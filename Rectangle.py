"""Create a Rectangle class that accepts width and height.

Implement:

__eq__ — rectangles are considered equal if their areas are equal;
__lt__ — one rectangle is less than another if its area is smaller."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
