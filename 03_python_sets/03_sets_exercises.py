# 1. Create a Set
my_set_fruits = {"apple", "pear", "cherry", "berry", "kiwi", "orange"}
print("\nPrint out 'my_set':", my_set_fruits)

# 2. Check Membership
print("\n--- Check if 'apple is in 'my_set_fruits'. ---")
if 'apple' in my_set_fruits:
  print("The word 'apple' is in 'my_set_fruits'.")
else:
  print("The word 'apple' is not in 'my_set_fruits'.")
  
# 3. Add an Update Items
my_set_fruits.add("peach")
print("\nAdd a new item to your set.")
more_fruits = {"grape", "melon", "strawberry"}
print("Print out the added item in the second set of fruits:", more_fruits)
my_set_fruits.update(more_fruits)
print("\nUpdate your first set with the second set of fruits:", my_set_fruits)

# 4. Remove Items
my_set_fruits.remove("pear")
print("\nRemove 'pear' from 'my_set_fruits':", my_set_fruits)
my_set_fruits.discard("bananas")
print("Remove 'banana' if it is in 'my_set_fruits' ifnot discard:", my_set_fruits)
removed_item = my_set_fruits.pop()
print("Removed item:", removed_item)
copy_set = my_set_fruits.copy()
copy_set.clear()
print("Copy your set and remove all items inside of with:", copy_set)

# 5. Set Operations
my_set_fruits_a = {"cherry", "berry", "kiwi", "orange", "strawberry"}
my_set_fruits_b = {"grape", "melon", "apple", "pear", "cherry", "berry"}

my_set_fruits_larger = my_set_fruits_a.union(my_set_fruits_b)
print("\nPrint out the larger Set() combined with the union() method:", my_set_fruits_larger)

# Intersection 
my_set_intersection = my_set_fruits_a.intersection(my_set_fruits_b)
print("\nPrint out Intersection of 'fruits_a' and 'fruits_b':", my_set_intersection)

#Reset the fruit sets
my_set_fruits_a = {"cherry", "berry", "kiwi", "orange", "strawberry"}
my_set_fruits_b = {"grape", "melon", "apple", "pear", "cherry", "berry"}

# Differences a
my_set_difference_a = my_set_fruits_a.difference(my_set_fruits_b)
print("\nPrint out the 'fruits_a' and find elements that are not in 'fruits_b':", my_set_difference_a)

# Differences b
my_set_difference_b = my_set_fruits_b.difference(my_set_fruits_a)
print("\nPrint out the 'fruits_b' and find elements that are not in 'fruits_a':", my_set_difference_b)

# Symmetric_differences
my_set_symmetric_diff = my_set_fruits_a.symmetric_difference(my_set_fruits_b)
print("\nPrint out differrence between 'fruits_a' and 'fruits_b':", my_set_symmetric_diff)

# 6. In-Place Set Operations
my_set_fruits_a.difference_update(my_set_fruits_b)
print("\nPrint out the different items that are in 'fruits_a' but not in 'fruits_b':", my_set_fruits_a)

#Reset the fruit sets
my_set_fruits_a = {"cherry", "berry", "kiwi", "orange", "strawberry"}
my_set_fruits_b = {"grape", "melon", "apple", "pear", "cherry", "berry"}

my_set_fruits_a.intersection_update(my_set_fruits_b)
print("\nPrint out common items between 'fruits_a' and 'fruits_b':", my_set_fruits_a)

#Reset the fruit sets
my_set_fruits_a = {"cherry", "berry", "kiwi", "orange", "strawberry"}
my_set_fruits_b = {"grape", "melon", "apple", "pear", "cherry", "berry"}

my_set_fruits_a.update(my_set_fruits_b)
print("\nUpdate() 'my_set_fruits_a with 'my_set_fruits_b' and print out:", my_set_fruits_a)

#Reset the fruit sets
my_set_fruits_a = {"cherry", "berry", "kiwi", "orange", "strawberry"}
my_set_fruits_b = {"grape", "melon", "apple", "pear", "cherry", "berry"}

# 7. Relational Methods

my_small_set = {"apple", "pear", "banana"}
my_large_set = {"cherry", "berry", "kiwi", "orange", "strawberry", "apple", "pear", "banana", "grape", "melon"}

my_issubset = my_small_set.issubset(my_large_set)
print("\nPrint out if 'my_small_set' is a subset of 'my_large_set':", my_issubset)

my_superset = my_large_set.issuperset(my_small_set)
print("\nPrint out if 'my_large_set' is a superset of 'my_small_set':", my_superset)

my_disjointset = my_large_set.isdisjoint(my_small_set)
print("\nPrint out if 'my_large_set' is disjoint with 'my_small_Set':", my_disjointset)