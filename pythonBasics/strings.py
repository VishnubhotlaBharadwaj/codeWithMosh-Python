course = "   Python Programming   "
print(len(course))
print(course[0])
print(course[-1])  # first character from end of the list

# Slicing a string
print(course[0:3])  # print first three indexes
print(course[:])  # print the entire string

# Since strings are immutable, after all these operations --> Initial value remains same

# Formatted Strings
first = "Bharadwaj"
last = "Vishnubhotla"

full = f"{first} {last}"
print(full)

# Useful string operations
print(course.upper())  # all characters to upper
print(course.lower())  # all characters to lower
print(course.title())  # first characters of everyword to upper
print(course.strip())  # trim extra white spaces (starting or end of string)
# --> we have lstrip and rstrip too
print(course.find("Pro"))  # returns Index of Pro
# --> If exact match not found.. returns -1
print(course.find("pro"))
print(course.replace("P", "-"))  # replace all P with -
