# Class: blueprint for creating new objects
# Object: Instance of a class
# Example:
# Class: Human
# Objects: John, Mary, jack etc..
# classes uses PascalNamingConvention

class Point:
    def draw(self):  # all functions in the classes should have atleast one parameter
        print("draw")


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))
