# list is a sequence of objects
# we can have a list of lists
# using '*' we can repeat the items in the list
zeros = [0] * 10  # prints 10 zeros

# '+' is used to concatenate two lists
# every object in list can be of different types
# list function is iterable
list(range(20))  # prints a list from 0 to 19

a = len(zeros)  # gives length of the list

# list is mutable
# during slicing a string we can pass a step too
l = [1, 2, 3, 4, 5, 6]
print(l[::2])

# list unpacking
# we can assign values of a list to different variable
# but, no. of variables in the left side should be equal to number of values in list
numbers = [1, 2, 3]
first, second, third = numbers

# we can also pack the unnecessary values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# prints first, pack all other into seperate list, prints last
first, *other, last = numbers

# loopimg over lists
# enumerate objects returns a tuples
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)
