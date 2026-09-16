# OOP Stands for Object Oriented Programming.
# Object: A collection of variables & functions. 
# Class: A blueprint for a specific object. 

# The importance of OOP is to create reusable codes. 

# Defining a Python class.
# We use the "class" keyword to create a class in Python. 

# Similar to functions:
def functionName():
    pass

# We can also create a class like this:
class ClassName:
    # class definition
    pass

# A simple class: 
class Bike:
    name = ""
    gear = 0 
    colour = ""

# Here, the bike is the name of the class, while the name/gear is the variables
# inside the class. 

# PYTHON OBJECTS:
# An object can also be an instance of the class. 

# BIKE 1
bike_1 = Bike()
bike_1.name = "BTWIN Folding"
bike_1.colour = "Gloomy Grey"

print(f"Name: {bike_1.name}, Colour {bike_1.colour}")

# BIKE 2
bike_2 = Bike()
bike_2.name = "Apollo City"
bike_2.colour = "Roaring Red"
print(f"Name: {bike_2.name}, Colour {bike_2.colour}")


# Exercise:
# Create a class called Car and it should have three attributes: name, color & type
# The type can be of electric/hybrid
# Then create two cars of different attributes then print them
