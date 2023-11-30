# handling exceptions

try:
    age = int(input("Age: "))
    factor = 10 / age
# except ValueError as x:
#     print("You didn't enter a valid age..!")
#     print(x)
#     print(type(x))
# except ZeroDivisionError:
#     print("Age is entered as Zero!")
except (ValueError, ZeroDivisionError) as x:
    print("You didn't enter a valid age..!")
    print(x)
    print(type(x))
else:
    print("No exceptions are thrown!!")
finally:  # used to close opened apps, database connections etc..
    print("Hero Hero Hero")

# with statement automatically closes the connection, irrespective of 'finally' clause

# raising exceptions


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less..!")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
