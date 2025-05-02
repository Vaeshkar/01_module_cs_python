# Create an initial dictionary

d = {"name" : "Alice", "age" : "30", "city" : "New York"}
print("Initial dictionary:", d)

# clear()
temp_d = d.copy() # copy and preserve original fo further demonstration
temp_d.clear()
print("\nPrint out 'temp_d' after clear():", temp_d)

# copy()
copied_d = d.copy()
print("\nCopied dictionary using copy():", copied_d)

# fromkeys()
keys = ["a", "b", "c"]
new_d = dict.fromkeys(keys, 0) 
print("Dictionary from key using fromkeys():", new_d)

keys_tel = ["verena_mobil", "dennis_mobil", "adriaan_mobil"]
new_d_tel = dict.fromkeys(keys_tel, "+49 1234567890")
print("\nDictionary from keys using fromkeys()_tel:", new_d_tel)

# get()
name_value = d.get("name")
missing_value = d.get("missing key", "Default")
print("\nValue of 'name' using get():", name_value)
print("Missing key returns default using get():", missing_value)

# pop()
age = d.pop("age")
print("\nPopped 'age':", age)
print("Dictionary after 'pop()':", d)

# popitem()
last_item = d.popitem()
print("\nPopped last item using 'popitem()':", last_item)
print("Dictionary after 'popitem()':", d)

# setdefault()
# Reset dictionary for further demonstration
d= {"Name" : "Alice", "age" : 30, "city" : "New York"}
age_value = d.setdefault("age", 40) # 'age' key exists, so returns existing value
country_value = d.setdefault("country", "USA") # 'country' key doesn't exist, so set and returns 'USA'
print("\nsetdefault() existing key 'age':)", age_value)
print("setdefault() knew key 'country':", country_value)
print("Dictionary after setdefault():", d)

# update()
d.update({"city" : "Boston", "occupation" : "Engineer"}) # update the whole dict with new keys and values
print("\nAfter update()", d)

# values()
values_list = list(d.values())
print("\nValues as list:", values_list)