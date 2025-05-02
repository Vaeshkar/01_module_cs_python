# Starting list
my_list = [3, 1, 4, 1, 5, 9]
print("Original list:", my_list)

# 1. append()
my_list.append(2)
print("nAfter append(2)", my_list)

# 2. clear() – We'll do this on a separate list to avoid losing data
temp_list = [10, 20, 30]
print("\nTemp list before clear:", temp_list)
temp_list.clear()
print("Temp list after clear():", temp_list)

# 3. copy()
copied_list = my_list.copy()
print("\nCopied list:", copied_list)

# 4. count()
ones_count = my_list.count(1)
print(f"\nCount of '1' in my_list: {ones_count}")

# 5. extend()
another_list = [7, 8, 9]
my_list.extend(another_list)
print("\nAfter extend([7. 8. 9])", my_list)

# 6. index()
index_of_4 = my_list.index(4)
print("\nIndex of '4':", index_of_4)

# 7. insert()
my_list.insert(1, "new")
print("\nAfter insert(1, 'new'):", my_list)

# 8. pop()
popped_item = my_list.pop() # By default, pops the last item
print("\nAfter pop() – removed item:", popped_item)
print("my_list after pop():", my_list)

popped_item_1 = my_list.pop(1) # Remove item at index 1
print(f"\nAfter pop(1) – removed item '{popped_item_1}' at index 1:", my_list)

# 9. remove()
my_list.remove(1) # REmove the first occurrence of 'new'

# 10. reverse()
my_list.reverse()
print("\nAfter reverse():", my_list)

# 11. sort()
my_list.sort()
print("\nAfter sort():", my_list)