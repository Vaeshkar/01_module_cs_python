class Car:
    # The __init__ method initializes a new Car object with given attributes
    # Also known as a constructor = special method
    def __init__(self, make, color):
        self.make = make # Property: make of the car
        self.color = color # Property: color of the car
        self.speed = 0 # Property: Default speed
        
    # Method to somilate accelerating the car
    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.color} {self.make} accelerates to {self.speed} mph.")
    
    # Method to simulate braking the car
    def brake(self, decrease):
        self.speed -= decrease
        print(f"The {self.color} {self.make} slows down to {self.speed} mph.")
    
    # Method to displey the car's current status    
    def status(self):
        print(f"{self.color.capitalize()} {self.make} is moving at {self.speed} mph.")

# Creating an object (instance) of the Car class
my_car = Car(make="Toyota", color="red") # Using positional arguments

# Accesing object properties and methods
my_car.status() # Display the status
my_car.accelerate(30) # Increase speed
my_car.brake(10) # Decrease speed
my_car.status() # Display the updates status

# Test examples
print(type(my_car)) # not sure why to use type()