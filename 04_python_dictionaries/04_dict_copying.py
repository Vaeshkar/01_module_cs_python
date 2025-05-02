# Original Dictionary

original_dict = {
  "name" : "Alice",
  "age" : 30,
  "hobbies" : ["reading", "cycling"]
}

print("\nOriginal dictionary:", original_dict)

# 1. Copying using copy() method
copy_dict_method = original_dict.copy()
print("\nCopied dictionary using copy():", copy_dict_method)

# 2. Copying using dict() constructor
copy_dict_constructor = dict(original_dict)
print("Copied dictionary using dict():", copy_dict_constructor)

# Verify that they are separate objects
# 'is' will return 'True' if two variables point to the same object (in memory), 
# '==' if the objects referred to by the variables are equal.
print("\nAre original and copy_dict_method the same objects?", original_dict is copy_dict_method) # False
print("\nAre original and copy_dict_constructor the same object?", original_dict is copy_dict_constructor) # False

# Modify original at top level
original_dict["age"] = 31
print("\nAfter modifying original_dict['age'] to 31:")
print("Original dictionary:", original_dict)
print("'copy_dict_method':", copy_dict_method)
print("'copy_dict_constructor':", copy_dict_constructor)

# Modify a mutable value inside the dictionary (list under "hobbies")
original_dict["hobbies"].append("painting")
print("\nAfter appending 'painting' to 'original_dict'['hobbies']:")
print("Original dictionary:", original_dict)
print("copy_dict_method:", copy_dict_method)
print("copy_dict_constructor:", copy_dict_constructor)

# Observations:
# – the 'age' change only affected the original dictionary because it's a top-level change.
# – the change in 'hobbies' is reflected in the copies as well because they share references to the same mutable list (shallow copy behavior).
