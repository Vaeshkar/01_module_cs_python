# Exercise 1: Basic Function
""" def greet():
    return "Hello, world!"
 
message = greet() 
print(message) """

# --------------
# Exercise 2: Function with Positional Arguments
""" def add(num1, num2):
    return num1 + num2

print(add(4, 6)) """

# --------------
# Exercise 3: Function with Data Validation
""" def calculate_area(width, height):
    if not isinstance(width, int) or not isinstance(height, int):
        return "Error: both width and height must be an integer."
    return width * height

print(calculate_area(14, "tr"))
print(calculate_area(5, 4)) """
 
# --------------   
# Exercise 4: Function with *args
""" def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result = num * result
        
    return result
print(multiply_all(4,5,6,6))
 """

# Exercise 5: Combining Positional, Keyword (Default) Arguments, and *args
# def greet_names(greeting="Hi", *names, punctuation="!"):
#     if not names:
#         return ["No names to greet."]
    
#     messages = [] # generate an empty list 
#     for name in names:
#         message = f"{greeting}, {name}{punctuation}" # generate a message string from the arguments
#         messages.append(message) # add the message in the list
    
#     return messages # returns

# print(greet_names("Halo", "John", "Bob", "Verena", punctuation="."))

# #Test cases
# greetings1 = greet_names("Hoi", "Mark", "Jeroen", "Bart")
# greetings2 = greet_names("Good Morning", "Dave", "Steve", punctuation=".")
# greetings3 = greet_names("Hi")
# print(greetings1)
# print(greetings2)
# print(greetings3)

# --------------
# Exercise 6: Extra Challenge – Simple Calculator with Variable Arguments

# def calculator(operator, *numbers):
#     # check if there are numbers
    
#     if not numbers:
#         return "Error: No numbers are entered."
#     # checks all numbers 'using all()' if they are an int or float.
#     if not all(isinstance(num, (int, float)) for num in numbers): 
#         return "Error: Input must be a number."
#     # checks if the operators are these given 4. 
#     if operator not in ('+', '-', '*', '/'):
#         return "Error: Invalid operator."
    
#     # handle the operators
    
#     # plus operator
#     if operator == "+":
#         return sum(numbers) #sums up the numbers with the build in sum() func and returns it directly.
    
#     # subtract operator
#     elif operator == "-":
#         result = numbers[0] # define a variable and assign an empty list.
#         for num in numbers[1:]: # start at the front and iterate true the numbers.
#             result -= num # take the result and update it with the subtract and current num.
#         return result # return the result back to the called function.
        
#     # multiply operator    
#     elif operator == "*":
#         result = 1 # define a variable and assign a number 1, not zero. 0*5 = 0, Zero is always a zero.
#         for num in numbers[1:]: # iterate over the numbers, starting from the first index.
#             result *= num # take the result and update it with the multiply and current num.
#         return result # return the result back to the called function.
    
#     # division operator 
#     elif operator == "/":
#         if 0 in numbers[1:]: # check if the first number is not 0.
#             return "Error: Division by zero is not allowed."
#         result = numbers[0] # create another var and assign it to an empty list.
#         for num in numbers[1:]: # iterate true the numbers, starting from position 1.
#             result /= num # take the result and update it with the divide and current num.
#         return result # return the result back to the called function.
        

# test_sum1 = calculator("+", 4, 3, 2)
# test_sum2 = calculator("-", 10, 8, 4)
# test_sum3 = calculator("*", 4, 14, 42)
# test_sum4 = calculator("/", 900, 6, 12)
# test_sum5 = calculator("/", 10, 0, 4) # test divide by 0.
# test_sum6 = calculator("%", 85, 43, 2) # test False operator
# test_sum7 = calculator("-") # Test error nu numbers
        
# print("The calculator result is:", test_sum1)

# --------------
# Exercise 7: Inventory System with Dictionary & Functions

# Instructions:

# You are building a simple inventory system for a store.

# Define a function manage_inventory that:

# Accepts two parameters:
# inventory (a dictionary where keys are item names and values are quantities).
# action (a string that can be "add", "remove", or "check").
# Uses keyword arguments (**kwargs) to handle multiple items at once.
# Function behavior:

# "add": Increase the quantity of items in the inventory.
# "remove": Decrease the quantity of items (but don’t allow negative values).
# "check": Return the current quantity of the requested item(s).
# If an invalid action is provided, return an error message.
# Test cases to try:

# store_inventory = {"apple": 10, "banana": 5, "orange": 8}

# manage_inventory(store_inventory, "add", apple=5, banana=3)
# manage_inventory(store_inventory, "remove", banana=2, orange=10)
# print(manage_inventory(store_inventory, "check", apple=True, banana=True))
# manage_inventory(store_inventory, "sell", grapes=10)  # Invalid action



# exercise
store_inventory = {"apple":10, "banana":5, "orange":8}

def manage_inventory(action: str, **inventory):
    
    if action not in ["add", "remove", "check"]:
        return "Error: Invalid action."
    
    if action == "add":
        for item, quantity in inventory.items():
           if item in store_inventory: # check if item is in store.
                store_inventory[item] += quantity
           else: 
               store_inventory[item] = quantity # adds item in store. 
    elif action == "remove":
        for item, quantity in inventory.items():
            if item in store_inventory: # also here check if item is in store.
                if store_inventory[item] >= quantity:
                    store_inventory[item] -= quantity
                else:
                    return "Error: Not enough stock."
            else:
                return f"Error: {item} doesn't exist in inventory."
    elif action == "check":
        return store_inventory
    
    return store_inventory
    

print(manage_inventory("add", banana=3, orange=6))
#print(manage_inventory("add", apple=5, banana=3))
#print(manage_inventory("remove", banana=2, orange=2))
#print(manage_inventory("check", apple=True, banana=True))
#print(manage_inventory("sell", grapes=10))  # Invalid action