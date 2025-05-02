# number = int(input("Please, give us a number: "))
# squares = []

# for i in range(1, number + 1):
#     squares.append(i ** 2)
    
# print(f"With the input you gave us. The squared list of {number} is here: {squares}. ")

# Task for You:
# Write a function that:

# Takes a number n as input.
# Returns a list of squared numbers from 1 up to n.
# Then call the function with a number and print the result. Let me know how it goes! 😊

# Steps
# 1 def a function that takes a parameter num 
# 2 create an empty list inside the func
# 3 set a range of numbers from 1 to num (inclusive)
# 4 loop over the range of numbers and square them
# 5 store the results in the list with append
# 6 call the function
# 7 print the result

# # create a func with a param num
# def square_number(num):
#     # create an empty list
#     numbers = []
#     # loops over the range of numbers 1 to num (inclusive)
#     for i in range(1, num + 1):
#         # stores the result in the list with append
#         numbers.append(i ** 2)
    
    
#     #return the numbers to the call
#     return numbers   


# # ask the user for input
# num_input = int(input("Enter a number to get a list of square numbers: "))

# # call the function
# result = square_number(num_input)

# # print the result
# print(f"The list of square numbers up to {num_input} is: {result}")

# # step 1
# list_of_five = [6,7,8,9,10]
# print(list_of_five)

# # step 2
# list_of_five.append(11)
# print(list_of_five)

# # step 3
# list_of_five.remove(6)
# print(list_of_five)

# # step 4
# list_of_five.pop(-1)
# print(list_of_five)

# # step 5
# print(f"the final list is: {list_of_five} and it has the following length:", len(list_of_five))

###########
# user_input_a = int(input("give me a number: "))
# user_input_b = int(input("give me another number: "))   
    

# print(f"The sum of {user_input_a} + {user_input_b} is:", user_input_a + user_input_b)
# print(f"The difference of {user_input_a} - {user_input_b} is:", user_input_a - user_input_b)
# print(f"The product of {user_input_a} * {user_input_b} is:", user_input_a * user_input_b)
# print(f"The one line division of {user_input_a} / {user_input_b} is:", user_input_a / user_input_b if user_input_b != 0 else 'Cannot divide by zero!')
# #build in a simple except with an if user_input_b is Not
# if user_input_b != 0:
#     print(f"The division of {user_input_a} / {user_input_b} is:", user_input_a / user_input_b)
#     print(f"The floor division of {user_input_a} // {user_input_b} is:", user_input_a // user_input_b)
#     print(f"The remainder of {user_input_a} % {user_input_b} is:", user_input_a % user_input_b)
# else:
#     print("Cannot divide by zero!")
# print(f"The power of {user_input_a} ** {user_input_b} is:", user_input_a ** user_input_b)

########### Same thing function ###########

def arithmetic_func(a, b):
    """This will use all arthmetic operators and return the values stored in a dict"""
    # create a dict
    arithmetic_sums = {
        "sum of a + b: ":0,
        "difference of a - b: ":0,
        "product of a * b: ":0,
        "divsion of a / b: ":0,
        "floor division of a // b: ":0,
        "remainder of a % b: ":0,
        "power of a ** b: ":0
    }
    
    # check for division by zero
    if b == 0:
        return "Error: cannot divide by zero."  # return error message as string
    
    try:
        arithmetic_sums["sum of a + b: "] = a + b
        arithmetic_sums["difference of a - b: "] = a - b
        arithmetic_sums["product of a * b: "] = a * b
        arithmetic_sums["divsion of a / b: "] = a / b
        arithmetic_sums["floor division of a // b: "] = a // b
        arithmetic_sums["remainder of a % b: "] = a % b
        arithmetic_sums["power of a ** b: "] = a ** b
         
    except Exception as e:
        return f"Unexpected Error: {e}."
    
    return arithmetic_sums

# call the function
test1 = arithmetic_func(5,9)
test2 = arithmetic_func(8,0)
test3 = arithmetic_func(2,19)

# check if the called func is a str or dict. Due to the division of zero check, returns a string.
if isinstance(test3, str):
    # check the results is a string (if error message)
    print(test3)
else:
    # if dictionary print it
    
    # gets the longest key length
    max_length = max(len(k) for k in test3.keys())
    
    # print the function
    print("\nArithmetic Results:")
    for key, value in test3.items():
        print(f"{key:<{max_length + 2}} {value}") # add 2 for extra spacing
        # < format specifier: Left align the text
        # > format specifier: Right align the text
        
        
######### Final Version #########
def get_max_key_length(d):
    """Calculates the longest key length in a dictionary."""
    if isinstance(d, dict):
        return max(len(k) for k in d.keys())
    return 0  # Return 0 if the input is not a dictionary

def print_arithmetic_results(results, max_length):
    """Checks if the result is a dictionary and prints it."""
    if isinstance(results, dict):
        print("\nArithmetic Results:")
        for key, value in results.items():
            print(f"{key:<{max_length + 2}} {value}")  # add 2 for extra spacing
    else:
        print("Error: the result is not a dictionary.")

def arithmetic_func(a, b):
    """
    This will use all arthmetic operators and return the values stored in a dict
    """
    # create a dict
    arithmetic_sums = {
        "sum of a + b: ": 0,
        "difference of a - b: ": 0,
        "product of a * b: ": 0,
        "divsion of a / b: ": 0,
        "floor division of a // b: ": 0,
        "remainder of a % b: ": 0,
        "power of a ** b: ": 0
    }

    # check for division by zero
    if b == 0:
        return "Error: cannot divide by zero."

    try:
        arithmetic_sums["sum of a + b: "] = a + b
        arithmetic_sums["difference of a - b: "] = a - b
        arithmetic_sums["product of a * b: "] = a * b
        arithmetic_sums["divsion of a / b: "] = a / b
        arithmetic_sums["floor division of a // b: "] = a // b
        arithmetic_sums["remainder of a % b: "] = a % b
        arithmetic_sums["power of a ** b: "] = a ** b

    except Exception as e:
        return f"Unexpected Error: {e}."
    return arithmetic_sums

# Function to handle multiple tests
def handle_multiple_tests(*test_cases):
    for a, b in test_cases:
        result = arithmetic_func(a, b)
        max_length = get_max_key_length(result)
        print_arithmetic_results(result, max_length)

# Multiple test inputs in one function call
handle_multiple_tests((5, 4), (10, 0), (3, 7), (6, 4))