
import math

# to print immaginery numbers
x = 1 + 2j  # j is like i in imaginery numbers
print(x)

# Division operation returns Quotient
# Modulo operation returns Remainder
# '/' performs divison
# '//' performs integer division
# Augmented assignment operator --> +=, -=
print(round(2.9))  # rounds to the nearest integer
print(abs(-2.9))  # prints absolute value of number

print(math.ceil(2.2))  # prints the next integer

# input() always accepts a string --> we need to typecast to get desired input
x = int(input("x: "))
print(type(x))
y = x + 1
print(f"x : {x}, y: {y}")

bool(0)  # gives false, anything else is true
