# Define some sample variables
x = 10
y = 20
z = 10
a = 5
b = 15

# Equal (==)
print("Is x equal to y?", x == y) # expected: False
print("Is x equal to z?", x == z) # expected: True

# Not equal (!=)
print("\nIs x not equal to y?", x != y) # expected: True
print("Is x not equal to z?", x != z) # expected: False

# Greater than (>)
print("\nIs y greater than x?", y > x) # expected: True
print("Is a greater than b?", a > b) # expected: False

# Lesser than (<)
print("\nIs x less than y?", x < y) # expected: True
print("Is b less than a?", b < a) # expected: False

# Greater than or equal to (>=)
print("\nIs x greater than or equal to z?", x >= z) # expected: True
print("Is y greater than or equal to b?", y >= b) # expected: True

# Less than or equal to (<=)
print("\nIs x less than or equal to z?", x <= z) # expected: True
print("Is a less than or equal to b?", a <= b) # expected: True

# Additional combined comparisons
print("\nIs x equal to 10 and y greater than 15?", (x == 10) and (y > 15)) # expected: True and True, meaning: True
print("Is a less than 10 or b greater than 100?", (a < 10) or (b > 100)) # expected: True and False, meaning: True