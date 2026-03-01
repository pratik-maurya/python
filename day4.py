# Conditionals
age = 20
if age < 18:
    print("You are a an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Combining conditions
name = "Pratik"
age = 25
if name == "Pratik" and age == 25:
    print("Welcome Pratik")

if age <18 or age > 60:
    print("Special Discount")

# While loop
count = 1
while count <= 5:
    print(f"count:{count}")
    count += 1

# Loop with range
for i in range(1, 6):
    print(f"i:{i}")

for i in range(0, 10, 2):
    print(f"i:{i}")


# Break and Continue
for i in range(1, 10):
    if i ==5:
        break
    print(f"i:{i}")

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(f"i:{i}")

# 🎯 Your Task
# Write a program that:

# Creates a list of numbers: [5, 12, 3, 18, 7, 25, 9, 30]
# Loops through and prints whether each number is even or odd
# Prints only numbers greater than 10
# Bonus: Find and print the largest number in the list without using max()

numbers = [5, 12, 3, 18, 7, 25, 9, 30]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

for num in numbers:
    if num < 10:
        print(f"{num} is less than 10")

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")
