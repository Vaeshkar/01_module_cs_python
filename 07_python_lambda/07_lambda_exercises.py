# Formula: Fahrenheit = (Celsius * 9/5) + 32
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)

numbers = list(range(1, 21))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)


# ----------
# 1. Basic Lambda for Addition

# var name: add
# create a lambda
# add two parameters
# return the sum
# test different pairs of numbers
# return the result inside a var and print it

add = lambda a, b: a + b
result = add(-15, 44) # results in 9

print(result)

# 2. Sorting with Lambda functions

# sort a list of tuples ascending
# use a lambda function inside a sorted() function
# return the sorted list and print it out

students = [("Alice",85), ("Bob",92), ("Charlie",78)] 
# Important: Tuples don't accept pairs but need commas instead to add 2 elements

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# create a var to save the data
# use sorted() function to sort the list ascending (default is false)
# insert the students var in the sorted() function.
# on the key parameter we set the lambda
# the lambda function is there to grab the student(tuple) in our list of students with:
# student is our argument and 
# student[1] is out expression to select the second position in our indexed tuple. In our example score value. 
