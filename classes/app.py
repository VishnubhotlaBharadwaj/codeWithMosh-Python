# Class: blueprint for creating new objects
# Object: Instance of a class
# Example:
# Class: Human
# Objects: John, Mary, jack etc..
# classes uses PascalNamingConvention

class Point:

    def __init__(self, x, y):  # constructor; self is the reference for current object
        self.x = x
        self.y = y

    def draw(self):  # all functions in the classes should have atleast one parameter
        print(f" Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
print(type(point))
print(isinstance(point, Point))
print(point.x)
print(point.y)
