# Dictionaries
person = {
    "name": "Pratik",
    "age": 25,
    "city": "Mumbai",
}
print(person["name"])
print(person["age"])

# Dictionary Methods
person["language"] = "Python"
person["age"] = 26
del person["city"]
print(person.keys())
print(person.values())
print(person.get("email", "Not Found"))

for key, value in person.items():
    print(f"{key}: {value}")


# 🎯 Your Task
# Write a program that:

# Creates a dictionary for yourself with keys: name, age, city, language, hobby
# Prints each value using the key
# Updates your age to next year
# Adds a new key email with your email
# Loops through the dictionary and prints all key: value pairs
# Bonus: Create a list of 3 friend dictionaries (name + city) and loop through them

myself = {
    "name": "Pratik",
    "age": 25,
    "city": "Mumbai",
    "language": "Python",
    "hobby": "Coding"
}

print(myself["name"])
print(myself["age"])
print(myself["city"])
print(myself["language"])
print(myself["hobby"])

myself["age"] = 26
myself["email"] = "pm@gmail.com"

for key, value in myself.items():
    print(f"{key}: {value}")

friends = {
    "Alice": {"age": 24, "city": "Delhi"},
    "Bob": {"age": 27, "city": "Bangalore"},
    "Charlie": {"age": 22, "city": "Chennai"},
}

for friend, details in friends.items():
    print(f"{friend} is {details['age']} years old and lives in {details['city']}.")