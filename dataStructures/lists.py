# list is a sequence of objects
# we can have a list of lists
# using '*' we can repeat the items in the list
zeros = [0] * 10  # prints 10 zeros

# '+' is used to concatenate two lists
# every object in list can be of different types
# list function is iterable
list(range(20))  # prints a list from 0 to 19

len(list)  # gives length of the list

# list is mutable
# during slicing a string we can pass a step too
l = [1, 2, 3, 4, 5, 6]
print(l[::2])
