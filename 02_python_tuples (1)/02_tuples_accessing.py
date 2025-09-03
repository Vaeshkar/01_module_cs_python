# Tuples accessing 
# 1. Creating a tuple
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print("Original tuple:", my_tuple)

# 2. Accessing items by index
print("First item (index 0):", my_tuple[0])
print("Last item (index -1):", my_tuple[-1])

# 3. Slicing the tuple
print("Items from index 1 to 3 (exclusive of 3):", my_tuple[1:3])
print("Items from the start up to index 2 (exclusive):", my_tuple[:2])
print("items from index 2 to the end:", my_tuple[2:])

# 4. Check if an item exists
if "banana" in my_tuple:
  print("'banana' is present in my_tuple")
else:
  print("'banana' is not in my_tuple")
  
  # 5. Demonstrating immutability
  # The following line would cause an error if uncommented, since tuples are immutable 
  #my_tuple[1] = "blueberry"
  
  # 6. Explicit conversion into a list
  temp_list = list(my_tuple)
  print("\nTemporary list conversion:", temp_list)
  
  # Example modifications: add, remove items
  temp_list.append("fig") # Adding an item
  temp_list.remove("cherry") # Removing an item
  temp_list[0] = "avocado" # Changing an item
  print("Modified list:", temp_list)