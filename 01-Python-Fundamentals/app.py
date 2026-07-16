import random
import math
print("Hello World")
print("*****")

x = 5
y = 10
unit_price = 4

# Variable

student_count = 1000
rating = 4.99
is_published = False
course_name = "python programming"
print(student_count)
print(rating)
print(is_published)
print(course_name)


# strings

course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:])

# Escape Sequences
# \"
# \'
# \\
# \n

course = "python \"programming"
print(course)

first = "siva"
last = "prasad"
full = first + " " + last
print(full)
full = f"{first} {last} is a good boy"
print(full)
full = f"{first} {last} is a good boy"

# Sting Methods
course = "    python programming"
print(course.upper())  # converts the string to uppercase
print(course.lower())  # converts the string to lowercase
print(course.title())  # capitalizes the first letter of each word
# removes whitespace from the beginning and end of the string
print(course.strip())
# returns the index of the first occurrence of the substring
print(course.find("p"))
# replaces all occurrences of the substring with another substring
print(course.replace("p", "j"))
# returns True if the substring is found in the string
print("python" in course)

print('swift' not in course)

# Numbers
x = 10
x = 1.1
x = 1 + 2j
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# working with numbers
x = 2.9
print(round(x))
print(abs(-2.9))

print(round(x))
print(abs(-2.9))

print(math.ceil(2.9))


# Type Conversion
x = 1  # int
y = float(x)  # converts int to float
z = str(x)  # converts int to string
print(y)
print(z)
print(type(y))
print(type(z))

# x = input("x:")
# print(type(x))  # this will print <class 'str'> because input() returns a string
# y = x + 1
# print(y)  # this will raise an error because x is a string and cannot be added

# Fundamentals of programming

# conditional statements
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


age = 22
if age >= 18:
    print("You are an adult")
else:
    print("You are a child")


age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators
# and
# or
# not

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")


# short-circuit evaluations
if high_income and good_credit and not student:
    print("Eligible for loan")

# chaining comparison Operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# FOr loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# for..else:

success = False
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# Iterables
for x in [1, 2, 3, 4, 5]:
    print(x)

print(type(5))  # <class 'int'>
print(type(range(5)))  # <class 'range'>


# while loops
i = 1
while i <= 5:
    print(i)
    i += 1

# infinite loops
# while True:
#     command = input(">")
#     if command.lower() == "quit":
#         break
#     else:
#         print("Unknown command")

# Exercise: Guess the number

# secret_number = random.randint(1, 10)
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess a number between 1 and 10: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed!")


# Functions
def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")


greet_user("Siva")

# arguments


def greet_user(name, age):
    print(f"Hi {name}!")
    print(f"You are {age} years old")
    print("Welcome aboard")


greet_user("Siva", 22)


# Type of Arguments
def greet_user(name, age=18):
    print(f"Hi {name}!")
    print(f"You are {age} years old")
    print("Welcome aboard")


greet_user("Siva")


# Type of functions

def square(number):
    return number * number


result = square(5)
print(result)

# keyword arguments


def greet_user(name, age):
    print(f"Hi {name}!")
    print(f"You are {age} years old")
    print("Welcome aboard")


greet_user(age=22, name="Siva")

# Default Arguments


def greet_user(name, age=18):
    print(f"Hi {name}!")
    print(f"You are {age} years old")
    print("Welcome aboard")


greet_user("Siva")

# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
