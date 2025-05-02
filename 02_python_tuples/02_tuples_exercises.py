# 1. Create a Tuple
my_tuple = ("fish", "dog", "cat", "bird", 5)

# 2. Print the Tuple
print("\nPrint out 'my_tuple':", my_tuple)

# 3. Access Tuple Items
print("\nPrint the first item of 'my_tuple':", my_tuple[0])
print("\nPrint the first item of 'my_tuple':", my_tuple[-1])

# 4. Slice the Tuple
print("\nPrint a slice of 'my_tuple' that includes some middle items:", my_tuple[1:3])
print("Print the index up to 3:", my_tuple[:3])
print("Print past the 2nd index:", my_tuple[2:])

# 5. Check if an Item exists
print("\nCheck if dog exists in 'my_tuple':", my_tuple)
if "dog" in my_tuple:
  print("The word 'dog' is in 'my_tuple'.")
else:
  print("The word 'dog' is not in 'my_tuple'.")
    
# 6. Count and Index
if 'cat' in my_tuple:
  print("\nThe word 'cat' is present in 'my_tuple'.")
else:
  print("\nThe word 'cat' is not present in 'my_tuple'.")
  
# 7. Packing and Unpacking
item1, item2, item3, item4, item5 = my_tuple
print("Basis Unpacking")
print(item1, item2, item3, item4, item5)

print("\nPrint out a tuple with an asterisk.")
(item1, item2, *others) = my_tuple
print("Asterisk on the last Variable:")
print("Item1:", item1)
print("Item2:", item2)
print("others from 'my_tuple':", others)

# 8. Joining Tuples
another_tuple = ("dragon", "snake", "gryphon")
longer_tuple = my_tuple + another_tuple
print("\nPrint the concatenated tuples:", longer_tuple)
multiplied_tuple = my_tuple * 2
print("print the multiplied tuple:", multiplied_tuple)