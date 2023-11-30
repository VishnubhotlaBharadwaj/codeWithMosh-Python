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

# lists can be sorted using list.sort()
# sorted in reverse using list.sort(reverse = True)
# sorted(list) --> creates a new sorted list without modifying the original list
# sort() dont take any possitional arguments, it takes only keyword arguments

# Map function is used to transform a list into a different list
items = [
    ("p1", 10),
    ("p2", 9),
    ("p3", 12),
]

prices = list(map(lambda item: item[1], items))

# filter function
filtered = list(filter(lambda item: item[1] >= 10, items))

# list comprehensions for line 47
prices = [item[1] for item in items]

# list comprehensions for line 50
filtered = [item for item in items if item[1] >= 10]

# Zip function --> combining multiple lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
