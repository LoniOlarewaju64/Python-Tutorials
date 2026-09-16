# What is polymophism? I'll explain.

# It can mean one thing, many forms or....one class 
# behaves differenctly based on how objects or classes 
# interact with it. 

# CODE IMPLEMENTATION:

class Cat:
    def info(self):
        print("I am a cat!")

    def make_sound(self):
        print("MEOW!")


class Dog:
    def info(self):
        print("I'm a dog!")

    def make_sound(self):
        print("WOOF!")


# OBJECT CREATION:
cat = Cat()
dog = Dog()

for animal in (cat, dog):
    animal.make_sound()