def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Bharadwaj", "Vishnubhotla")
greet("John", "Smith")

# parameter is the input defined for the function
# argument is the actual value of the parameter
# functions are of two types --> 1. Perform a trask, 2. Return a value
# In python all functions returns the value none, unless you specifically returns a value

# keyword arguments


def increment(number, by):
    return number + by


print(increment(2, by=1))

# default arguments


def increment(number, by=1):
    return number + by


print(increment(2, 7))

# variable number of arguments (xargs)


def multiply(*numbers):
    print(numbers)
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)
