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

# #Mutable and Immutable Types:
# x = [1, 2, 3]
# print(id(x))
# x.append(4)
# print(id(x))

# #Strings:

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[::-1])

# #Escape Sequences:

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

# #Formatted Strings:

# first = "Rabbi Hossain"
# last = "Rakib"
# full = first + " " + last
# full2 = f"{first} {last}"
# print(full)
# print(full2)

# #Usefull String Methods:

# course = "Python Programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())  # to remove extra unwanted space
# print(course.find("Pro"))
# print(course.replace("P", "-"))

# print("Programming" in course)
# print("Programming" not in course)

# #Numbers:

# x = 1023
# print(bin(x))
# print(hex(x))
# print(oct(x))

# y = 1+2j  # j is imaginary i in python
# print(y)

# #Arithmatic Operators:

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

# #Working with Numbers:

# import math
# PI = 3.1416
# x = 5
# print(round(PI))
# print(math.factorial(x))
# print(math.floor(PI))

# #Type_conversion:

# x = input("x: ")
# y = x+1
# print(y)

# #Conditional_Statements:

# age = int(input())
# if age >= 18:
#     print("adult")
# elif age >= 13:
#     print("Teenagee")
# else:
#     print("Child")
# print("All Done!")

# #Ternary Operator:

# age = 22
# if age >= 18:
#     message = "eligable"
# else:
#     message = "not eligible"

# message = "Eligible" if age >= 18 else "Not eligible"

# print(message)

# #LOOPS:

# for x in "Python":
#     print(x)
# for x in ['a', 'b', 'c']:
#     print(x)

# #For...else:

# names = ["ARakib", "Prisha"]
# for name in names:
#     if name.startswith("R"):
#         print("Found")
#         break
# else:
#     print("Not Found")

# #While_loops:

# gues = 0
# answer = 5
# while answer != gues:
#     gues = int(input("Guess: "))

# #function:
# def increment(number, by):
#     return number+by


# print(increment(2, 3))

# #Arguments:

# def multiply(*list): #python will read *list as a tuple
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# #Arguments xxargs:

# def save_user(**user):
#     print(user)


# save_user(id=1, name="rakib") # output is dictionary

# #Debugging :

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")

# #Exercise:

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "fizzbuzz"
#     if input % 3 == 0:
#         return "fizz"
#     if input % 5 == 0:
#         return "buzz"
#     return input


# print(fizz_buzz(30))

# #Lists:
# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0]*5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("hello world")
# print(len(chars))

# #Accessing items of a list:

# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0: 3: 1])

# numbers = list(range(20))
# print(numbers[::-1])

# #Lists unpacking:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a, b, *other, c = x
# print(a)
# print(b)
# print(c)
# print(other)

# #Looping over Lists:
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     # enumerate generates tuple with index number.
#     print(index, letter)

# Adding and removing items in Lists:

# letters = ["a", "b", "c", "e", "f", "g"]
# # Add
# letters.append("d")
# letters.insert(0, "-")

# # Remove
# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# letters.clear()
# print(letters)

# #Finding Items in Lists:

letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))
