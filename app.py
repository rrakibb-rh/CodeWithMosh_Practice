# ***getting started:

# print("hello World")
# x = (2 + 1)
# print(x)

# ***Variables:

# students_count = 1000
# rating = 4.99
# is_published = False
# course_name = """
# Multiple
# lines
# """
# x, y = 1, 2

# ***Dynamic Typing:
# print(type(1.1))
# print(type(123))
# print(type(True))

# ***Mutable and Immutable Types:
# x = [1, 2, 3]
# print(id(x))
# x.append(4)
# print(id(x))

# ***Strings:

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[::-1])

# ***Escape Sequences:

# \"
# \'
# \\
# \n
# msg = '''Python
# is
# a
# great
# programming
# language'''
# print(msg)

# ***Formatted Strings:

# first = "Rabbi Hossain"
# last = "Rakib"
# full = first + " " + last
# full2 = f"{first} {last}"
# print(full)
# print(full2)

# ***Usefull String Methods:

# course = "Python Programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())  # to remove extra unwanted space
# print(course.find("Pro"))
# print(course.replace("P", "-"))

# print("Programming" in course)
# print("Programming" not in course)

# *** Numbers:

# x = 1023
# print(bin(x))
# print(hex(x))
# print(oct(x))

# y = 1+2j  # j is imaginary i in python
# print(y)

# *** Arithmatic Operators:

# x = 10+3
# x = 10-3
# x = 10*3
# x = 10/3
# x = 10//3
# x = 10 % 3
# x = 10**3
# x = x+1
# x += 1
# print(x)

# Working with Numbers:

# import math
# PI = 3.1416
# x = 5
# print(round(PI))
# print(math.factorial(x))
# print(math.floor(PI))

# Type_conversion:

# x = input("x: ")
# y = x+1
# print(y)

# Conditional_Statements:

age = int(input())
if age >= 18:
    print("adult")
elif age >= 13:
    print("Teenagee")
else:
    print("Child")
print("All Done!")
