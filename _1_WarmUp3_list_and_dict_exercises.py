# 1. List Creation and Basic Access
# countries = ["Country_01", "Country_02", "Country_03", "Country_04", "Country_05"]
# print(countries)
# print(countries[2])
# countries[-1] = "Country_06"
# print(countries[-1])
# print(countries.append("Country_00"))
# countries.pop(0)
# print(countries)
# print(len(countries))
# print(countries.sort())

# 2. Dictionary Creation and Basic Access
# student = {
#     "name":"Alice",
#     "age":25,
#     "grades":[75, 46, 97]
#     }
# print(student)
# print(student["name"])
# print(student["grades"][1])
# student["age"] += 1
# print(student)
# student["city"] = "New York"
# print(student)
# student.pop("city")
# print(student)

# 3. Working with a List of Dictionaries
# peoples = [
#   {"name":"Stephan","age":15,"city":"Amsterdam"},
#   {"name":"Kenny","age":18,"city":"Eindhoven"},
#   {"name":"Mark","age":28,"city":"Brussels"}
# ]
# print(peoples)
# for people in peoples:
#   print(f"Name: {people["name"]}, Age: {people["age"]}")
  
# # create a variable:
# older_person_age = 0
# for people in peoples:
#   if people["age"] > older_person_age:
#     print("check age:", older_person_age)
#     older_person_age = people["age"]
# print("found oldest age:", older_person_age)

# # 3.2 Extra stretch goal: find and print the average age of all people
# age = [age["age"] for age in peoples] # <-- List comprehension
# print(age) # check and print all ages
# average_age = sum(age) / len(age) # add all ages and divide them with the length of all ages.
# print(average_age) # print average_age var

# 5. Deeply Nested Dictionary Navigation
# university = {
#     "name": "Some University",
#     "departments": {
#         "Computer Science": {
#             "professors": [
#                 {"name": "Malan", "specialty": "CS50"},
#                 {"name": "Lee", "specialty": "Cybersecurity"}
#             ],
#             "courses": ["Algorithms", "Machine Learning"]
#         },
#         "Mathematics": {
#             "professors": [
#                 {"name": "Johnson", "specialty": "Statistics"},
#                 {"name": "Patel", "specialty": "Algebra"}
#             ],
#             "courses": ["Calculus", "Linear Algebra"]
#         }
#     }
# }

# print(university["name"])
# print(university["departments"])
# print(university["departments"]["Computer Science"]["professors"][0]["name"])

# 5.2 Iterate through all professors in all departments and print their names and specialties.
# for dept in university["departments"]:
#   for prof in university["departments"][dept]["professors"]:
#     print(f"Name: {prof["name"]} – {prof["specialty"]}.")

# 5.3 Print all courses across all departments
# for courses in university["departments"]:
#   for course in university["departments"][courses]["courses"]:
#     print(course)

# Final Challenge: Build Your Own Data Structure
# company = {
#   "name":"Walk this way inc.",
#   "department": {
#     "design":{
#       "employees":[
#         {"employee_name":"Dennis", "position":"worker"},
#         {"employee_name":"Venus", "position":"director"}
#       ],
#       "projects":["Project_one", "Project_two"]
#       },
#     "packaging": {
#         "employees": [
#             {"employee_name":"Julien", "position":"Designer"},
#             {"employee_name":"Mark", "position":"Desktop Publisher"}
#         ],
#         "projects": ["Box Redesign"]
#     },
#     "management": {
#         "employees": [
#             {"employee_name":"Bart", "position":"CTO"},
#             {"employee_name":"Wolfgang", "position":"CFO"}
#         ],
#         "projects": ["Budget Planning"]
#     }
#   }
# }
# Print company name
# print(f"Company name: {company["name"]}")

# # Print all departments
# print("\nDepartments:")
# for dept in company["department"]:
#   print(f"– {dept}")
  
# # Print all employees with positions
# print("\nEmployees:")
# # When we call .items() on a dictionary, it gives us both the keys and values.
# for dept, details in company["department"].items(): #dept = key and details = value, in combination with .items()
#   for person in details["employees"]:
#     print(f"– {person["employee_name"]} _ {person["position"]}.") 
    
# # Print all projects across all departments
# print("\nProjects:")
# for dept, details in company["department"].items():
#     for project in details["projects"]:
#         print(f"– {project}")  # See what this prints!
        
        
my_numbers = list(range(17))
print(my_numbers)
target_num = 7


len(my_numbers) / 2

def binarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found