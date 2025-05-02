# Creating a nested dictionary
person = {
  "name" : "Alice",
  "age" : 30,
  "address" : {
    "city" : "New York",
    "zipcode" : "10001",
    "coordinates" : {
      "latitude" : 40.7128,
      "longitude" : -74.0060
      }
    },
  "occupation" : "Engineer"
}

# Accessing top-level elements
print("Name:", person["name"])
print("Age:", person["age"])

# Accessing nested dictionary elements
address = person["address"]
print("\nAddress:", address)

city = person["address"]["city"]
print("City:", city)

zipcode = person["address"]["zipcode"]
print("Zipcode:", zipcode)

# Accessing deeper nested elements
latitude = person["address"]["coordinates"]["latitude"]
longitude = person["address"]["coordinates"]["longitude"]
print("Coordinate:", latitude, longitude)

# Using get() to safely access nested values
# This example tries to access a non-existent key with a default value
country = person.get("address", {}).get("country", "Country not specified.")
print("Country:", country)

# Using get() for deep nested retrieval with potential missing keys
# Notice we use cascading get() calls, each with default empty dict{}
lat_safe = person.get("address", {}).get("coordinates", {}).get("latitude", "No latitude")
print("Safe Latitude Access:", lat_safe)