# Functions can be passed as arguments
def my_func(func):
    print('This is the first function')
    func()
    
def another_func():
    print('This is another function')
    
my_func(another_func) 
# Important: calling another function inside as a argument is without parentheses

# Functions can be returned from another function and stored in variables
def multiply_by_n(multiplier):
    def multiply(number):
        print(multiplier * number)
    return multiply

multiply_by_two = multiply_by_n(2)
multiply_by_three = multiply_by_n(3)

multiply_by_two(4)
multiply_by_three(4)

# Assigning a lambda function to a variable
square = lambda x: x * x
print(square(5)) # outputs: 25 form=5*5
print() # blank line

# Refactor our multiply_by_n example
def multiply_by_n_lambda(multiplier):
    return lambda number: print(multiplier * number)

multiply_by_five = multiply_by_n(5)
multiply_by_six = multiply_by_n(6)

multiply_by_five(4)
multiply_by_six(4)