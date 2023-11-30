# Stack --> Last In First Out (LIFO)
# .append() to add items in the last
# .pop() to remove items from the last

# Queue --> First IN First Out (FIFO)
# If there are many objects in the queue, removing the first element make the other elements to shift one position left which leads to performance issues
# To tackle the above problem --> we use Dequeue method
# to remove first element --> .popleft() is used

# Tuples --> read only list, we cannot modify existing objects
# () is used to define a tuple

# swapping values
from array import array
x, y = 10, 11
x, y = y, x
print(x, y)

# arrays --> specify the type
# Use this only when dealing with large set of numbers
num = array("i", [1, 2, 3])

# Sets --> removing the duplicates
# supports the huge library of mathematics
# set doesnot support index. i.e, we cannot access items with index
numbers = [1, 1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)  # symmetric difference

# Dictionaries --> key, value pairsx
point1 = {'x': 1, 'y': 2}
point2 = dict(x=1, y=2)
print(point2['x'])

# looping over dictionaries
for key, value in point2.items():
    print(key, value)

# dictionary comprehensions
values = {x: x*2 for x in range(5)}
print(values)

# Generator Expressions
# These are iterable; at easy iteration it spit out a new value
# These store nothing in the memory

# Unpacking operator
numbers = [1, 2, 3]
print(*numbers)
# --> we can unpack any iterable objects
