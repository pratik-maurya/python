# A list stores multiple values in one variable
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])
print(fruits[-1])

# List Methods 
languages = ["Python", "JavaScript", "C++"]
languages.append("Java")
languages.remove("C++")
languages.insert(1, "Django")
print(len(languages))
print(languages[0:2])

# Looping through a list
for lang in languages:
    print(lang)

# 🎯 Your Task
# Write a program that:

# Creates a list of 5 of your favorite movies
# Prints the first and last movie
# Adds one more movie to the list
# Removes one movie
# Prints the total count of movies
# Loops through and prints all movies

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
print(f"First Movie is {favorite_movies[0]}")
print(f"Last Movie is {favorite_movies[-1]}")
favorite_movies.append("Avatar")
favorite_movies.remove("The Matrix")
print(f"Total Movies: {len(favorite_movies)}")
for movie in favorite_movies:
    print(movie)
