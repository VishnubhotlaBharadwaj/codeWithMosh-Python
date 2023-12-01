# Class: blueprint for creating new objects
# Object: Instance of a class
# Example:
# Class: Human
# Objects: John, Mary, jack etc..
# classes uses PascalNamingConvention
# Objects in python are dynamic, we dont have to define all of them in the constructor
class Point:
    # class level attribute,  can be accessed by all the objects of the class
    default_class = "blue"

    def __init__(self, x, y):  # constructor; self is the reference for current object
        self.x = x
        self.y = y

    def draw(self):  # all functions in the classes should have atleast one parameter
        print(f" Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

print(Point.default_class)
print(point.default_class)
