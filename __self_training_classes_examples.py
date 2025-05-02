#### Class ############## example 1

# class Car:
#     """This is a class about cars and stuff"""
    
#     wheels = 4 # Class attr
    
#     def __init__(self, brand, model, year):
#         self.brand = brand # Instance attr
#         self.model = model # Instance attr
#         self.year = year # Instance attr
        
#     def car_info(self):
#         return f"\nCar Info: \n–{self.brand}, \n–{self.model}, \n–{self.year}. \nIt has {self.wheels} wheels.\n"
  
#     @classmethod # new class method
#     def change_wheels(cls, new_wheels_count):
#         cls.wheels = new_wheels_count
        
#     @staticmethod
#     def basic_info():
#         return "\nCars are a transportation system"
    
#     def __str__(self):
#         return f"\nThis is a {self.brand} {self.model} fromt he year {self.year}."


# # Instance 1      
# car = Car("Ford", "Shelby", 1967)
# # call the car info
# print(car.car_info())

# Car.change_wheels(6)

# # Instance 2
# car2 = Car("Ford","F-150", 2024)
# # call tnhe car info 2
# print(car2.car_info())

# print(car2) #prints the defined __str__


#### Class ############## example 2

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sey_hello_from_student(self):
#         return f"\nHello, my name is {self.name} and my age is {self.age}."
    
#     @classmethod
#     def taking_notes(cls):
#         return "\nAll students take notes!"
    
# # Class Method
# print(Student.taking_notes())

# linus = Student("Linus", 30)
# # Instance Method
# print(linus.sey_hello_from_student())


#### Class ############## example 3

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
        
#     def deposit(self, amount):
#         self.__balance += amount
#         return f"\nThe new balance is: {self.__balance}."
    
#     def withdraw(self, amount):
#         self.__balance -= amount
#         return f"\nThe new balance is: {self.__balance}."
    
#     def get_balance(self):
#         return f"\nThe {self.owner} balance is: {self.__balance}."
    
# bob_account = BankAccount("Bob", 1000)
# print(bob_account.get_balance)

# print(bob_account.withdraw(500))


# bob_account.balance = 999999999999999

# print(bob_account.get_balance())

#### Class ############## example 4

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    # instance method
    def get_info(self):
        return f"The car year: {self.year} and brand: {self.brand}."

# abstract from another class   
class Airplane(Vehicle):
    def __init__(self, brand, year, plane_code):
        super().__init__(brand, year) # calling the parent class constructor
        self.plane_code = plane_code
        
    def get_info(self):
        return f"{super().get_info()} Plane Code: {self.plane_code}"
    
my_airplane = Airplane("spitfire", 1940, "HS-89F")
    
print(my_airplane.get_info())