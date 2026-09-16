"""
Python Inheritance allows us to create a class from an existing one.

Super Class, a parent class/general class & Sub Classes.

"""

#Super Class
class Animal:
    name = "unknown"

    def eat(self):
        print ("i CAN eat :).")

# Sub Class 
# Inherit from Animal Class

class Dog(Animal):

    def display_name(self):
        print("My name is...", self.name)

class Cat(Animal):

    def display_name(self):
        print("My name is...", self.name)

labrador = Dog()
labrador.name = "Berry"
labrador.eat() # Method from the inheritied/super class.
labrador.display_name() # Method from the class. 

# Inheritance is an 'is - a' relationship.
# Examples:
# Dog is an Animal
# Cat is an Animal 
# Car is a Vehicle

# Method Overriding 

class Animal:
    name = "unknown"

    def eat(self):
        print("I can eat.")

class Dog(Animal):

    # Method overrriding the eat method from the class it was inherited from...

    def eat (self):
        print("I like to eat bones.")

    def display_name(self): 
        print("My name is", self.name)

labrador = Dog()
labrador.name = "Mario"
labrador.eat()

"""
There are 5 types of Inheritance:
1. Single: A child class inherits from only one parent class. 

2. Multiple: A child class inherits from multiple parent classes. 

3. Multilevel: A child class inherits from its parent class which is inheriting
from another parent class. 

4. Hierarchical: More than one child class are created from a single parent class. 

5. Hybrid: This combines more than one form of inheritance. 



"""
