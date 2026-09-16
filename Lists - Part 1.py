
#This is a regular, relevant list. 
fruits = ["apple", "banana", "cherry"]

#This has random items included. A phrase, a date and a program phrase.
random_mixed_list = ["Heya!", True, 3.14, 2026]

#This list is empty. Nothing. Nada.
empty = []
empty = list()

#This is a nested list. Can contain any kind of data.
matrix = [[[1, 2]], [3,4]]


#3.14 is for 'pi'
#year = 2026, an integer.

# print(type(pi))
# print(type(year))


#Here's an example of usage of Lists:

# 1. Accessing List Items (Indexing and Slicing)
fruits = ["apple" "banana", "cherry," "grapes", "blueberries"]

#Indexing
print(fruits[0]) # --> 0 --> apple, first item
print(fruits[1])
print(fruits[-1]) #last item in the list

#Slicing
print(fruits [0:3]) #0, 1, 2 
print(fruits [2:]) #outputs from cherry to the end...
print(fruits[1:]) #outputs from banana to the end...
print(fruits[:3]) #outputs from beginning of list till index 3
print(fruits[::-1]) #Reverses the list....

# 2. Modifying Lists
colours = ["red", "green", "blue"]
colours[1] = "purple"
print(colours)


#3. List Methods
#Adding Methods
items.append('c') # Adds to the end of the list 
items.insert(2, "x") # Inserts 'x' at position 2. 
items.extend(["d", "e"])
print(items)