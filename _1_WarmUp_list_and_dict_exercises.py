# 1. List Creation and Basic Access
print("\n# 1. List Creation and Basic Access")
l = ["Netherlands", "Germany", "Belgium", "Denmark", "Sweden", "Poland"]
print("\nPrint country list:", l)

print("Print ouf the 3rd country:", l[2])

l[-1] = "Norway"
print("Print out the changed country list:", l)

l.append("Poland")
print("Print out after append():", l)

l.remove("Netherlands")
print("Print out after remove():", l)
# .pop() method uses a specified index
# .remove() method uses a specified value

l_len = len(l)
print("Print out the length:", l_len)

l.sort()
print("Print out sort():", l)

# 2. Dictionary Creation and Basic Access
print("\n# 2. Dictionary Creation and Basic Access")
d = {
  "name" : "Dennis", 
  "age" : 46, 
  "grades" : [5, 3, 1, 2]
  }
print("\nPrint out dictionary:", d)
print("Print out dict 'name':", d["name"])
print("Print out the 2nd grade:", d["grades"][1])
d.update({"age" : 47})
print("Print out updated dict", d)
d["city"] = "Eindhoven"
print("Print out city in dict:", d["city"])
d.pop("city")
print("Print out the pop() in dict:", d)

# 3. Working with a List of Dictionaries
classroom_d = [
  {
    "name" : "Reagan",
    "age" : 36,
    "city" : "Berlin"
  },
  {
    "name" : "Abiy",
    "age" : 32,
    "city" : "Cologne"
  },
  {
    "name" : "Dennis",
    "age" : 46,
    "city" : "Glueckstadt"
  },
  {
    "name" : "Linus",
    "age" : 30,
    "city" : "Cologne"
  },
  {
    "name" : "Konstantin",
    "age" : 35,
    "city" : "Frankfurt"
  },
  {
    "name" : "Phoebi",
    "age" : 36,
    "city" : "Berlin"
  },
  {
    "name" : "Yuiia",
    "age" : 27,
    "city" : "Berlin"
  },
  {
    "name" : "Julien",
    "age" : 29,
    "city" : "Duesseldorf"
  }
]
print("\nPrint the whole list:", classroom_d)
for person in classroom_d:
  print(f"Name: {person["name"]}, Age: {person["age"]}")

people = [
    {"name": "Bobby", "age": 25, "city": "Berlin"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Danny-san", "age": 28, "city": "Tokyo"}
]
oldest_person_age = 0
for person in people:
  if person["age"] > oldest_person_age:
    oldest_person_age = person["age"]
print("\nPrint out the oldest age inside of People:", oldest_person_age)

#reduced iterating method
oldest_person_age = people[0]["age"] # goes to the first list item and selects the dict key: 'age'
for person in people[1:]: # Start iterating past the first index item in the list.
  if person["age"] > oldest_person_age:
    oldest_person_age = person["age"]
print("\nPrint out the oldest age inside of People:", oldest_person_age)

# 3.5 Extra stretch goal: find and print the average age of all people
# There are two ways. Julien and Linus showed you
age = [person["age"] for person in people] # This is called > list comprehension
print("Print out the list of age:", age) # Print out the age list

average_age = sum(age) // len(age) 
# Code breakdown: 
# Make a new variable: average_age.
# Assign it to a 'sum(iterable(r), start(o))' function that will return a number of alle iterated items. Iterable object(age).
# Then divide it with a division '/'. If we want rounded numbers we use floor_division '//'.
# Use the 'len(object(r))' function to find the length of our list, insert the needed object(age).
# Print out the variable: average_age to see the calculated numbers.
print("The average age of the people's list is:", average_age)


# 4. Navigating a Nested Dictionary
company = {
  "name":"Evil Inc",
  "city":"Los Angeles",
  "employees":[
    {"name":"Bob", "position":"Engineer", "salary":90000},
    {"name":"Bobby-San", "position":"Manager", "salary":120000},
    {"name":"Karol", "position":"Designer", "salary":85000},
  ]
}
print(f"Company name: {company["name"]}")
print("Number of employees: ", len(company["employees"]))
print("Name of the 2nd employee:", company["employees"][1]["name"])

for person in company["employees"]:
  #print(person)
  print(f"Employee name: {person["name"]} and position: {person["position"]}.")

print(company["employees"])

salary = [sal["salary"] for sal in company["employees"]]
print("\nSalary in company:", salary)
average_salary = sum(salary) // len(salary)
print("\nAverage salary is:", average_salary)

# 5. Deeply Nested Dictionary Navigation
university = {
  "name":"WBS University",
  "departments": {
    "Computer Science": {
      "professors": [
        {"name":"Malan Jefferson", "specialty":"CS50"},
        {"name":"Lee Bruce", "specialty":"Cybersecurity"}
      ],
      "courses": ["Algorithms", "Machine Learning"]
    },
    "Mathematics": {
      "professors": [
        {"name":"Johnson Stevens", "specialty":"Statistics"},
        {"name":"Patel Reinheart", "specialty":"Algebra"}
      ],
      "courses": ["Calculus", "Linear Algebra"]
    }
  }
}

# 5.1 Print the name of the university
print("\nPrint Uni name:", university["name"])

# 5.2 Print a list of all departments
# first solution. 
print("\nPrint a list of all departments:", list(university["departments"].keys()))
# cleaner and second solution
for dept in university["departments"]:
  print("Print a list of all departments:", dept)
  
# 5.3 Print the name of the first professor in the Computer Science department
print("\nFirst professor in \nComputer Science class:", university["departments"]["Computer Science"]["professors"][0]["name"])
  
# 5.4 Iterate through all professors in all departments and print their names and specialties.
print("\nPrint Professors and Specialties:")
for dept in university["departments"]:
  for prof in university["departments"][dept]["professors"]:
    print(f"{prof['name']} – {prof['specialty']}")
    
# 5.5 Print all courses across all departments
courses_list = [] # create an empty course list
for dept in university["departments"]: # loop true the departments
  courses_list.extend(university["departments"][dept]["courses"])
  # use list.extend(iterable(r)) to connect  
  # all the found courses into the courses_list

print(f"We teach the following courses: {' | '.join(courses_list)}")
# string.join(iterable) is used to connect all found courses to one string
# the separator ' | ' before join is used so the courses have a better reading form

# Final Challenge: Build Your Own Data Structure
