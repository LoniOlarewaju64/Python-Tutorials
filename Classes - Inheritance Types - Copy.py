# This is a follow up of Classes. We're going to look into types of Inheritances
# from last week's lesson. 

# SINGLE INHERITANCE: Only one parent & one child. 

# Parent
#class Animal:
    #def eat(self):
        #print("Animal eats...")

# Child 
#class Dog(Animal):
    #def bark(self):
        #print("Dog barks")

# dog = Dog()
# dog.eat()
# dog.bark()


# MULTIPLE INHERITANCE: One child, multiple parents.

# Parent
#class Dad:
    #def cooks(self):
        #print("Dad cooks...")

# Parent 
#class Mum:
    #def spars(self):
        #print("Mum spars...")

# Child 
#class Child(Dad, Mum):
    #pass

#child = Child()
#child.cooks()
#child.spars()


# MULTILEVEL INHERITANCE: GRANDPARENT -> PARENT -> CHILD.

#class Animal:
    #def eat(self):
        #print("The animal eats...")

#class Dog(Animal):
    #def bark(self):
        #print("...the dog barks....")

#class CutePuppy(Dog):
    #def play(self):
        #def play(self):
            #print("...and the puppy plays!")

#puppy = CutePuppy()
#puppy.eat()
#puppy.bark()
#puppy.play()


# HYBRID INHERITANCE: Combines two or more types of inheritance on coding
# An example: Multilevel & Multiple.

class Animal:
    def eat(self):
        print("Animal eats...")

class Dog(Animal):
    def eat(self):
                                    