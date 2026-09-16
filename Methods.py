"""
Python Methods 

"""

# Let's create a class. 

class Room: # This is the room plan, it can either be a study, living or a bedroom. 
    length = 10 # m 
    breadth = 10 # m

    def calculate_area(self):
        print("Area of Room = ", self.length * self.breadth) 



study_room = Room()
study_room.length = 40
study_room.breadth = 30

study_room.calculate_area()

bedroom = Room()
bedroom.length = 50
bedroom.breadth = 40

bedroom.calculate_area()
