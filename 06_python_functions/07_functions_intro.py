# Define a function that greets a user by name
def greet(name):
    print(f"Hello, {name}! Welcome to Python functions.")


# Define a function that checks if a number is even or odd
def check_even_odd(number):
    if number %2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is uneven.")
    
    
# Define a function that prints numbers from 1 to n using a loop
def print_numbers(n):
    print(f"Printing numbers from 1 to {n}:")
    for i in range(1, n + 1):
        print(i, end=" ")
    print() #blank line

# Define a function that sums a list of numbers
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"The sum of {numbers} is {total}.")
    
# Using the functions defined above
greet("Alice")
check_even_odd(7)
print_numbers(5)
sum_list([1, 2, 3, 5, 6])