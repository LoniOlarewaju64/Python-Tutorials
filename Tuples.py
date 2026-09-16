# This was noted on 28/06/2026.

"""

A tuple in coding is a built-in python data structure used to store
a collection of items in a single variable.

They're similar to lists. 

CHARACTERISTICS: 
1. Unchangeable once created unlike lists & dictionaries.
2. They're ordered. Each item has a specific postion. 
3. They allow duplicates.


"""

# BASIC SYNTAX 
# Creating a tuple - we use '()'


weekdays = ("Monday", "Tuesday", "Wednesday")
user_profile = ("Alice", 25, True)

#Tuples - Accessing Items:

fruits = ("apple", "banana", "cherry")
# print(fruits[0])
# print(fruits[-1])

# Tuples - Unpacking
player = ("PixelNinja", 1500, "Emerald")
username, score, rank = player
print(username)
print(score)
print(rank)

# Tuples - Their Methods
# The only two methods are: count & index. 

grades = ("A", "B", "C", "D", "E", "F")
print(grades.count("D")) # Counts how many items a value appears.
print(grades.index("F")) # Get the position of an item.

# Exercise
# Create a tuple that contains your name, favorite food & color
# Unpack them into their separate variables