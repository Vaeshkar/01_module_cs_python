# Lists: exercises

# 1. Create and print a list
my_list = [10, 15, 20, 55, 80, 110]
print("This is 'my_list' printed out:", my_list)

# 2. Access Elements by Index and Negative Idex
print("\nPrint the first item from 'my_list':", my_list[0])
print("Print the last items from 'my_list':", my_list[-1])

# 3. Slice a List
print("\nPrint a subset items from 'my_list':", my_list[1:3])
print("Print everything from up to index 2:", my_list[:2])
print("Print everything from index 2:", my_list[2:])

# 4. Check if an Item exists
if 20 in my_list:
  print("\nThe number 20 is found in 'my_list'.")
else:
  print("The number 20 is not found in 'my_list'.")
  
# 5. Add Items
my_list.append(5)
print("\nAppend a new number into 'my_list':", my_list)
my_list.insert(-1, 330)
print("Inset a new number with a index position to 'my_list':", my_list)

# 6. Change Items
my_list[-1] = 440
print("\nChange an item in 'my_lists':", my_list)

# 7. Remove Items
my_list.remove(55)
print("\nRemove an item from 'my_lists':", my_list)

my_list.pop(3)
print("Remove an item from a specific position in 'my_list':", my_list)

my_list.clear()
print("Clear the contents of 'my_list' with clear():", my_list)

#regenerate the cleared list once more
my_list = [10, 15, 20, 110, 330, 440]

# 8. Copy a List
my_list_copy = my_list.copy()
my_list_copy.clear()
my_list_copy = [5, 20, 25, 35, 220, 220, 550]

print("\nCopy 'my_list', change numbers and print out the copied list:", my_list_copy)
print("To compare here is the original 'my_list':", my_list)

# 9. Concatenate and Extend a list
my_list_extend = my_list + my_list_copy
print("\nConcatenate the two lists to one larger list:", my_list_extend)
my_list.extend(my_list_copy)
print("Also use the extend() method to combine the two lists:", my_list)

# 10. Sort and Reverse
print("\nOriginal list of numbers:", my_list)
my_list.sort()
print("Sorted in-place (ascending):", my_list)

my_list_desc = sorted(my_list, reverse=True)
print("Descending order 'my_list_desc':", my_list_desc)

# 11. Count and Index
my_list.count(0)
print(f"\nCount how many times 0 is in 'my_list':", my_list)
index_of_5 = my_list.index(5)
print("Print ouf the index of 5 from 'my_lists':", my_list)

# 12. List Comprehensions
my_list_fruits = ["banana", "apple", "cherry", "blueberry", "pears", "date", "oranges"]
five_letter_fruits = [fruit.upper() for fruit in my_list_fruits if len(fruit) <= 5]
print("\nOriginal fruits:", my_list_fruits)
print("Fruits with Five letters in them, in uppercase:", five_letter_fruits)