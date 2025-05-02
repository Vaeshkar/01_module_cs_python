# 1. List Creation and Basic Access
""" countries = ["DE", "NL", "BE", "UK", "DK"]
print(countries)
print(countries[2])
countries[-1] = "CH"
print(countries)
countries.append("FR")
print(countries)
print(len(countries))
countries.sort()
print(countries) """

# 2. Dictionary Creation and Basic Access
""" student = {
  "name":"Dennis",
  "age":46,
  "grades":[1, 3, 5, 7, 2]
}

print(student)
print(student["name"])
print(student["grades"][1])
student["age"] +=1
print(student["age"])
student["city"] = "Glueckstadt" # add a new item
print(student)
student.pop("city")
print(student)
 """
# 3. Working with a List of Dictionaries
""" students = [
  {
    "name":"Dennis",
    "age":46,
    "city":"Glueckstadt"
  },
  {
    "name":"Julien",
    "age":32,
    "city":"Berlin"
  },
  {
    "name":"Reagan",
    "age":36,
    "city":"Cologne"
  }
]
 """
""" print(students)
for person in students:
  print(f"Name: {person["name"]} and Age: {person["age"]}")
   """
# 3.5 Extra stretch goal: find and print the average age of all people
""" age = [chicken["age"] for chicken in students]
print(age)

average_age = sum(age) // len(age)
print(f"The average age of the students is: {average_age}")
 """
# 4. Navigating a Nested Dictionary
""" company = {
    "name": "Evil Inc",
    "location": "Los Angeles",
    "employees": [
        {"name": "Bob", "position": "Engineer", "salary": 90000},
        {"name": "Bobby-san", "position": "Manager", "salary": 120000},
        {"name": "Karol", "position": "Designer", "salary": 85000}
    ]
}

print(company["name"])
print(len(company["employees"]))
print(company["employees"][1]["name"])
for employee in company["employees"]:
  print(f"Name: {employee["name"]} and position: {employee["position"]}")
  
salary = [chicken["salary"] for chicken in company["employees"]]
average_salary = sum(salary) // len(salary)
print(average_salary)
 """
# 5. Deeply Nested Dictionary Navigation
university = {
    "name": "Some University",
    "departments": {
        "Computer Science": {
            "professors": [
                {"name": "Malan", "specialty": "CS50"},
                {"name": "Lee", "specialty": "Cybersecurity"}
            ],
            "courses": ["Algorithms", "Machine Learning"]
        },
        "Mathematics": {
            "professors": [
                {"name": "Johnson", "specialty": "Statistics"},
                {"name": "Patel", "specialty": "Algebra"}
            ],
            "courses": ["Calculus", "Linear Algebra"]
        }
    }
}

""" # 5.1 Print the name of the university
print(university["name"])


# 5.2 Print a list of all departments
departments = university["departments"].keys()
print(f"List of all the departments:", list(departments))

# 5.3 Print the name of the first professor in the Computer Science department
print(university["departments"]["Computer Science"]["professors"][0]["name"])
 """
# 5.4 Iterate through all professors in all departments and print their names and specialties.
for dept in university["departments"]:
  for prof in university["departments"][dept]["professors"]:
    print(f"Name: {prof["name"]} and specialty: {prof["specialty"]} ")
 
# 5.5 Print all courses across all departments
for dept in university["departments"]:
  for course in university["departments"][dept]["courses"]:
    print(f"We teach the following courses: {course}")

# Final Challenge: Build Your Own Data Structure
