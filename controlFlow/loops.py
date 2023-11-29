for number in range(3):
    print('Hi', number + 1)

for number in range(0, 4):
    print('Hi', number + 1)

for number in range(0, 10, 2):
    print('Hi', number + 1)

# for - else loop
successful = False
for i in range(3):
    print("Attempted")
    if successful:
        print("Successful")
        break
else:
    print(f" Attempted {i+1} times but Unsucessful")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# range function returns a object of the type range
print(type(range(5)))  # <class 'range'>

# range function is iterable
# strings are also iterable in python
for x in "Python":
    print(x)

# Lists are also iterable
for x in [1, 2, 3, 4]:
    print(x)
