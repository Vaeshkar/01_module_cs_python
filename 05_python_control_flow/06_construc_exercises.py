import random
import time

num = random.random() # generate a random number between 0 and 1
#print(num)

""" # 1. Basic If Condition
positive_number = 1
zero_number = 0
negative_number = -1
numbers = random.randrange(-5, 5)
#print(numbers)
print("\nPrint a random number and check if it is pos, neg or zero:")
if numbers > 1:
  print(f"Number {numbers} is a positive number.")
elif numbers == 0:
  print(f"Number {numbers} is a zero.")
else:
  print(f"Number {numbers} is a negative number.") """

""" # 2. Grade Calculator
score = random.randrange(0, 110, 10)
#print(score)
print("\nPrint a random number and check the score and grade it:")
if score == 0:
  print(f"Your grade is a F, with a score of: {score}.")
elif score <= 20 and score >= 1:
  print(f"Your grade is a D, with a score of: {score}.")
elif score <= 40 and score >= 21:
  print(f"Your grade is a C, with a score of: {score}.")
elif score <= 60 and score >= 41:
  print(f"Your grade is a B, with a score of: {score}.")
elif score <= 80 and score >= 61:
  print(f"Your grade is a A, with a score of: {score}.")
else:
  print(f"Your grade is a A+, with a score of: {score}.")
 """
 
""" # 3. Ternary Operator Practice
def check_age_movie():
  age = random.randrange(10, 99, 1)
  print("\nHello and good day,")
  time.sleep(0.6) # simulate a delay.
  print("to watch this movie you must be over 18. Checking your age:")
  time.sleep(0.4) # simulate a delay.
  print("         -   ------   -")
  print("          ..checking.. ")
  print("         -   ------   -")
  time.sleep(1.6) # simulate a delay.
  print("          Please wait. ")
  print("         -   ------   -")
  time.sleep(1.2) # simulate a delay.
  print("≈≈≈≈≈ ≈≈≈ Age Checked ≈≈≈ ≈≈≈≈≈")
  print(f"\n You are a minor(age: {age}) and \n cannot start watching. Sorry." if age <= 19 else f"\n  You are an adult(age: {age}), \n   have fun watching. Next!")
  print("\n ≈≈≈ ≈≈≈≈≈≈≈≈ ≈≈≈ ≈≈≈≈≈≈≈≈ ≈≈≈ ")
  time.sleep(0.8) # simulate a delay.
  print("\n... Program shutting down ...")
  time.sleep(0.6) # simulate a delay.
  print("--- - - --- -BYE- --- - - ---")

check_age_movie() """

""" # 4. For Loop over a List
cars = ["Mercedes", "Opel", "Porsche", "Volvo", "Toyota", "Renault", "Peugeot", "Range Rover"]

for car in cars:
  print(f"The cars in this list are: {car}.") # Print inside a scope
  
print(f"The cats in this list are the following: {', '.join(cars)}.") # print outside a scope and use .join() to print out the list contents onto one line. """

""" # 5. For Loop with Conditions
for num in range(11):
  if num % 2 == 1: # division by 2 and find remainders. 
    continue # loop over the uneven numbers
  print(num) # print out the even numbers. 
print() # blank line

for nim in range(21):
  if nim % 2 == 0:
    continue
  print(nim)
print() # blank line """

# 6. While Loop Summation
""" def function(name: str): # <- parameter = undefined
  # forcing the parameter to be a string with : and str
  return f"name is {name}"

print(function("Dennis")) # <- argument = defined  """
# 7. Break out of a Loop

""" list_of_words = ["word", "sting", "bottle", "airplane", "bicycle", "automobile", "apartment"]

for word in list_of_words:
  if len(word) > 5:
    break
print(word) """


# 8. Nested Loops
""" people = ["Dennis", "Julien", "Linus", "James"]
pets = ["Bird", "Cat", "Dog", "Fish"]

for person in people:
  print(f"{person} can choose the following pets:")
  for animal in pets:
    print(f" – {animal}")
  print() #blank space after the second for loop.
 """
# 9. Loop with 'Else' Clause
""" print("In written text, please write a number between one to ten:")
value_searching = ["five", "four", "three", "seven", "eight", "nine", "ten", "one", "two"]
for value in value_searching:
  if value == "seven":
    print(f"\nbreak! \nSuccess you have found the correct number: '{value}'.")
    break
  else:
    print(f"Sorry, that was not the correct number, please try again. \nNumber found: '{value}'")
 """
# 10. Pass Statement Usage
""" for item in []:
  pass # No action is taking, but syntactically value
 """

# 11. Pattern matching
""" list_fruits = ["banana", "apple", "pear"]
list_veggies = ["broccoli", "potato", "cucumber"]
list_meat = ["sausage", "steak", "drumsticks"]

item = "steak"

match item:
  case _ if item in list_fruits:
    print(f"{item} is a fruit.")
  case _ if item in list_veggies:
    print(f"{item} is a vegetable.")
  case _ if item in list_meat:
    print(f"{item} is a meat.")
  case _:
    print(f"{item} is something completely else.") """