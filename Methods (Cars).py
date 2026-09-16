# Create a class/blueprint for a Car
class Car:
    make = "Unknown"
    model = "Unknown"
    speed = 0

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.make} {self.model}, Current Speed: {self.speed} km/h")

    # Method to simulate accelerating
    def accelerate(self, increment):
        self.speed += increment
        print(f"Accelerated by {increment} km/h.")


# Create an instance (object) of the class
my_car = Car()
my_car.make = "Tesla"
my_car.model = "Model 3"

# Calls the  built methods
my_car.display_info()
my_car.accelerate(50)
my_car.display_info()