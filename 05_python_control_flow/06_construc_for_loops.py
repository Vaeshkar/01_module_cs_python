# Looping over a list
my_list = [1, 2, 3, 4]
print("Iterating over a list:")
for item in my_list:
  print(f"List item: {item}")
print() # Blank line for readability?

# Looping over a tuple
my_tuple = ('apple', 'banana', 'cherry')
print("Iterate over a tuple:")
for fruit in my_tuple:
  print(f"Tuple fruit: {fruit}")
print() # Blank line

# Looping over a dictionary by keys
my_dict = {
  "name":"Alice",
  "age":30,
  "city":"New York"
}
print("Iterate over a dictionary (keys):")
for key in my_dict:
  print(f"Key: {key}, Value: {my_dict[key]}")
print()

# Looping over a dictionary using items() to get key-value pairs directly
print("Iterating over a dictionary with items():")
for key, value in my_dict.items():
  print(f"{key}: {value}")
print() # Blank line

# Looping over a set
my_set = {10, 20, 30, 40, 50}
print("Iterating over a set:")
for num in my_set:
    print(f"Set number: {num}")
print() # blank line

# Looping over a string
my_string = "Hello"
print("Iterating over a string:")
for char in my_string:
  print(f"Character: {char}")
print() # blank line

# Using range() in a 'for' loop to generate a sequence
print("Using range() to iterate over a sequence of numbers:")
for i in range(5):
  print(f"Number from range: {i}")
print() # blank line

# Loop with 'continue'
for num in range(5):
  if num == 3:
    continue # Skips the rest of this iteration when num equals to the set == int.
  print(num)
print()

# Loop with 'break'
for num in range(3):
  print(num)
else:
  print("Loop completed without a break.")
print()

# Nested loop
words = ["apple", "banana", "cherry", "watermelon"]
target_letter = "n"
print("Words containing the letter 'n':")
for word in words:
  for letter in word:
    if letter == target_letter:
      print(f"{word} contains '{target_letter}'.")