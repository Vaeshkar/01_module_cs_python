# Dictionary Operations Demo

# Create an example dictionary

my_dict = {
  "name" : "Alice",
  "age" : 30,
  "city" : "New York"
}
print("\nInitial Dictionary:", my_dict)

# Accessing elements
print("\n--- Accessing Elements ---")
print("\nUsing scuare brackets, name:", my_dict["name"])
print("Using get(), country:", my_dict.get("country", "Not Found"))
print("Using get(), city:", my_dict.get("city", "Not Found"))
print("\nAll keys:", list(my_dict.keys())) # make a list from this dictionary and print out all keys
print("\nAll values:", list(my_dict.values())) # make a list from this dictionary and print out all values
print("\All items:", list(my_dict.items())) # make a list from this dictionary and print out all items

# Changing elements
print("\n--- Changing Elements ---")
my_dict["age"] = 31 # item assignment
print("After changing age:", my_dict)
my_dict.update({"city" : "Boston", "email" : "alice@example.com"})
print("\nAfter Update:", my_dict)

# Adding elements
print("\n--- Adding Elements ---")
my_dict.update({"occupation" : "Engineer"})
print("\nAfter adding occupation with update():", my_dict)

# Removing elements
print("\n--- Removing Elements ---")
# value = my_dict.pop("key_to_remove", "default_if_not_found")
removed_age = my_dict.pop("age", None)
print("Removed Age value:", removed_age)
print("Dictionary after pop():", my_dict)

# removes the last inserted item from the dictionary, since Python 3.7+
last_item = my_dict.popitem()
print("\nPopped last item:", last_item)
print("Dictionary after popitem():", my_dict)

# Adding more items for deletion demonstration
my_dict["hobby"] = "cycling"
print("\nBefore deletion:", my_dict)
del my_dict["city"]
print("After del my_dict['city']:", my_dict)

my_dict.clear()
print("\nAfter clear:", my_dict)

# Note: You can also delete the entire dictionary with 'del my_dict',
# but then my_dict will no longer exist, so further operations would fail. 
