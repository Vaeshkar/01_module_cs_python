# 1. Create and Print a Dictionary
print("\n# 1. Create and Print a Dictionary")
d = {"name" : "Alice", "age" : "30", "city" : "New York"}
print("\Print out dictionary:", d)

# 2. Access Dictionary Elements
print("\n# 2. Access Dictionary Elements")
print("Print out dict['name']:", d["name"])
email = d.get("email", "No email yet.") # Get syntax dict.get(keyname, value)
print("Print out dict['email']:", email)
print("Print out all dict.keys:", d.keys())
print("Print out all dict.values:", d.values())
print("Print out all dict.items()", d.items())

# 3. Check for Key Existence
print("\n# 3. Check for Key Existence")
print("Print out if 'age' is in dict:", "age" in d)

# 4. Change and Update Dictionary Elements
print("\n# 4. Change and Update Dictionary Elements")
d["city"] = "Boston"
d.update({"name":"Denise", "age":"41", "occupation":"Engineer"}) 
#Note to self: use curly brackets once if you update multiple keys and values. 
print("Print out updates on dict['city']:", d)

# 5. Add New Item to the Dictionary
print("\n# 5. Add New Item to the Dictionary")
d["country"] = "USA"
d.update({"hobby":"cycling"})
print("Print out the updates dict['country', 'hobby']:", d["country"], "and",  d["hobby"])

# 6. Remove Items from the Dictionary
print("\n# 6. Remove Items from the Dictionary")
removed_item = d.pop("name")
print("Print out after pop('name):", d)

popitem_d = d.popitem()
print("Print out popitem(), returns the last item:", popitem_d)

del d["city"]
print("Print out after del pair in dict:", d)
del d
print("Cannot print out after whole del of a dict.")

d = {"name" : "Alice", "age" : "30", "city" : "New York", "hobby":"cycling", "occupation":"Engineer", "country":"USA"}

# 7. Copy a Dictionary
print("\n# 7. Copy a Dictionary")
shallow_d = d.copy()
shallow_d["name"] = "Dennis"
print("Print out the copy dict:", shallow_d)
print("Print out the original dict:", d)

# 8. Using setdefault()
print("\n# 8. Using setdefault()")
setdefault_d = d.setdefault("name")
print(d)
print("Print out name with setdefault():", setdefault_d)
setdefault_d = d.setdefault("height", "Not yet defined") # adds a new key with a default message
print("Print out new key 'height' with setdefault():", setdefault_d)
print(d) # Test if the new key is added and shown in the dict
d["height"] = 6.1
print(d)
