# 1. Sequential Execution: instructions run one after another
print("Starting program")
a = 5
b = 10
sum_ab = a + b 
print("\nThe sum of", a, "and", b, "is.", sum_ab)

# Decision Making with if-elif-else
if sum_ab > 10:
    print("The sum is greater than 10.")
elif sum_ab == 10:
    print("The sum is exactly 10.")
else:
    print("The sum is less than 10.")
    
# 2. Pattern Matching (Python 3.10+)
day = 3
print("\nUsing pattern matching for day number:")
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Another day")

# 3.1 Repetition: 'For' Loop
print("\nFor Loop over a list to find favourite fruits:")
fruits = ['cherry', 'banana', 'apple'] # generate a variable with a lists[] of three string values
for fruit in fruits: # loop/iterate over the fruits(var)_list[] and save the values into fruit(var)
  print(f"I really like {fruit}.") # print the current fruits found with a f-string.
# the printed out values will be: I really like cherry., I really like banana., I really like apple.
  
# 3.2 Repetition: 'While' Loop
print("\nWhile loop until count reaches 5:")
count = 0 # set empty int variable
while count < 5: # do a whole loop to check if the count(int) is lesser than set int value(5)
  print(count) # print the current count value(int)
  count += 1 # if the value is not yet achieved add one count(int) with plus 1 (+=)
# the printed out values will be 0, 1, 2, 4
