# Day 1: Python Basics — Variables & Data Types
name = "Pratik"
age = 25
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print(type(name))
print(type(age))
print(type(is_student))

# String Operations
first_name ="Pratik"
last_name = "Maurya"

full_name = first_name + " " + last_name
print("Full Name:", full_name)

print(f"My name is {first_name} and I am {age} years old.")
print(name.upper())
print(name.lower())
print(name.replace("a", "@"))
print(len(name))

# 🎯 Your Task (Do this now!)
# Write a program that:

# Stores your name, age, city, and favorite programming language in variables
# Prints a sentence using f-string like: "Hi, I'm Ahmed, I'm 25 years old, from Karachi and I love Python!"
# Print the type of each variable

my_name = "Pratik"
my_age = 25
my_city = "Mumbai"
my_favourite_language = "Python"
print(f"Hi, I'm {my_name}, I'm {my_age} years old, from {my_city} and I love {my_favourite_language}!")
print(type(my_name))
print(type(my_age))
print(type(my_city))
print(type(my_favourite_language))