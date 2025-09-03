def add(a, b):
    return a + b
try:
    add(1)
except Exception as e:
    print(e)
    
def square(x): # parameter set is x
    return x * x # arg is 4 * 4
result = square(4) # result will be 16. 

def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet("Reagan", "Howdy") # Positional Arguments, prints: Howdy, Reagan!

greet(greeting="Hi", name="Alice") # Keyword Arguments, prints: Hi, Alice!

greet(name="Bob", greeting="Hello") # Keyword arguments, prints: Hello, Bob!

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Bob") # Prints: Hello, Bob! sing the default greeting
greet(name="Bob", greeting="Howdy") # Prints, Howdy, Bob!

def collect_with_args(*my_arbitrary_args):
    print(type(my_arbitrary_args))
    print(my_arbitrary_args)
    
collect_with_args(1, 2, 3) # Prints: class: tuple > (1, 2, 3)