# # 1. List Creation and Basic Access
# # 1
# countries = ["Germany", "Poland", "Denmark", "Netherlands", "England"]
# print(f"1. create a list of 5 countries:\n{countries}\n")
# # 2
# print(f"2. print the third country:\n{countries[2]}\n")
# #3 
# countries[-1] = "France"
# print(f"3. Change the last country in the list with a new one:\n{countries}\n")
# #4
# countries.append("England")
# print(f"4. append a country:\n{countries}\n")
# #5
# countries.remove("Germany")
# print(f"5. remove a country:\n{countries}\n")
# # 6
# len(countries)
# print(f"6. the length of the countries list: {len(countries)}.")
# #7
# countries.sort()
# print(f"7. sort the countries list:\n{countries}\n")

# # 2. Dictionary Creation and Basic Access
# # 1 
# student = {
#     "name": "Dennis", 
#     "age": 46,
#     "grades": [5, 7, 10]
# }
# # 2
# print(f"1. Student dictionary:\n{student}\n")
# # 3
# print(f"2. students name: {student['name']}.")
# # 4
# print(f"3. studen 2nd test score: {student['grades'][1]}")
# # 5
# print(f"4. student age + 1: {student['age']+1}.")
# # 6
# student.update({"city": "Eindhoven"}) # Update method
# student["country"] = "Netherlands" # new index + value
# print(f"5. new key 'city':\n{student}\n")
# # 7
# student.pop("city", None) # using .pop("key", None) safe removal, avoids KeyError
# #del student["city"] # using del, preferred
# print(f"6. remove the city key: {student}")

# # 3. Working with a List of Dictionaries
# # 1
# students = [
#         {"name":"Julien", "age":35, "city": "Paris"},
#         {"name":"Frank", "age":55, "city": "Hamburg"},
#         {"name":"Watzu", "age":40, "city": "Tokyo"}
#     ]
# # 2
# print(f"Print list of students: {students}")
# # 3
# for student in students:
#     print(f"\nStudent name: {student['name']} and age: {student['age']}.")
# # 4
# oldest_person = students[0]
# for person in students:
#     if person['age'] > oldest_person['age']:
#         oldest_person = person
# print(f"\nThe oldest student is {oldest_person['name']} with {oldest_person['age']} years.")   
# # 5  
# ages = [person['age'] for person in students] 
# average_age = sum(ages) / len(ages)
# print(f"\nthe average age of the students is: {average_age:.2f} years.")

# # 5. Deeply Nested Dictionary Navigation
# # 1
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
# print(f"1. University name: {university['name']}\n")
# # 2
# for department in university["departments"]:
#     print(f"The departments: {list(university['departments'].keys())}\n")
# # 3
# first_prof = university['departments']['Computer Science']['professors'][0]["name"]
# print(f"Name of the first Professor in Computer Science: {first_prof}.\n")
# # 4
# print("4. Professors and their Specialities.")
# for department in university['departments'].values():
#     for professor in department["professors"]:
#         print(f"   {professor['name']} - {professor['specialty']}")
# # 5
# all_courses = []
# for department in university["departments"].values():
#     all_courses.extend(department['courses'])
# print(f"\n5. All Courses Offered: {all_courses}.\n")

# # Final Challenge: Build Your Own Data Structure
# # 1
# # 2
# company = {
#     "name": "Dennis does code inc.",
#     "departments":{
#         "engineering":{
#             "employees":[
#                 {"employee_name":"Dennis", "position":"Founder"},
#                 {"employee_name":"Verena", "position":"Administration"},
#                 {"employee_name":"Adriaan", "position":"Designer"}
#                 ],
#             "projects":[
#                 "Corporate Design",
#                 "Backery Kniesmeijer",
#                 "Townhall website update"
#             ]
#         },
#         "marketing": {
#             "employees":[
#                 {"employee_name":"Dietlind", "position":"CFO"},
#                 {"employee_name":"Robert", "position":"Facility Manager"},
#                 {"employee_name":"Laura", "position":"Public Relations"}
#                 ]
#              ,
#             "projects":[
#                 "Social Media 2025",
#                 "New Business",
#                 "Market relevance"
#             ] 
#         }
#     }
# }
# #3
# print(f"Company name: {company['name']}\n")
# #4 
# for deparment in company["departments"]:
#     print(f"Company departments: {deparment}.\n")
# # 5
# for department_name, deparment_data in company["departments"].items():
#     print(f"\nDepartment: {department_name}")
    
#     for employee in deparment_data["employees"]:
#         print(f"– {employee['employee_name']} ({employee['position']})")
 