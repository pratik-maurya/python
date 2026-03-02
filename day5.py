def greet(name):
    print(f"Hello, {name}!")

greet("Pratik")
greet("Alice")


# Return values
def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")

def greet(name, message = "Hello"):
    print(f"{message}, {name}")
greet("Pratik")
greet("Alice", "Hi")

def get_info():
    name = "Pratik"
    age = 25
    return name, age
name, age = get_info()
print(name, age)

def get_even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
numbers = [1, 2, 3, 4, 5, 6]
print(get_even_numbers(numbers))


# 🎯 Your Task
# Write a program with these functions:

# greet_user(name, city) — prints "Hello Pratik, welcome from Mumbai!"
# calculate_area(length, width) — returns area of a rectangle
# find_largest(numbers) — takes a list, returns the largest number (reuse your yesterday's logic!)

# Yesturdays code
def largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [5, 12, 3, 18, 7, 25, 9, 35]
print(f"The largest number is: {largest(numbers)}")


def greet_user(name, city):
    print(f"Hello {name}, welcome from {city}!")
greet_user("Pratik", "Mumbai")

def calculate_area(length, width):
    return length * width
area = calculate_area(5, 3)
print(f"The area of the rectangle is: {area}")

def find_largest(numbers):
    largest_number = largest(numbers)
    if largest_number % 2 == 0:
        is_even = True
    else:
        is_even = False
    return largest_number, is_even
largest_number, is_even = find_largest(numbers)
print(f"The largest number is: {largest_number}, Even: {is_even}")

def is_even(number):
    return number % 2 == 0  # returns True or False directly

print(is_even(4))   # True
print(is_even(7))   # False

def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Pratik", 25)           # uses default
describe_person("Alice", 22, "Delhi")   # overrides default