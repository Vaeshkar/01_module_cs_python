# Creating a dictionary to represent a person
# Dictionary syntax:
# name_var = {"key" : "value", "Key2": "Value2"}

person = {
  "name" : "Alice",
  "age" : 30,
  "city" : "New York",
  "occupation" : "Engineer"
}

# Printing the entire dictionary
print("\nPerson dictionary:", person)

# Accessing values using keys
print("\nName:", person["name"])
print("Age:", person["age"])

# Changing a value
person["age"] = 31
print("\nAge(new):", person["age"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("\nAdded email:", person)

# Removing a key-value pair
del person["city"]
print("\nAfter removing city:", person)