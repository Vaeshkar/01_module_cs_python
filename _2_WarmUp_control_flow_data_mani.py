# Exercise 1: For Loop with Continue and Break
""" number_list = list(range(16))
for num in number_list:
    #print(num)
    if num % 3 == 0:
        continue
    if num > 10:
        break
    else:
        print("the current number:", num)

print(num) """  

# Exercise 2: While Loop with Continue, Break, and Else
""" counter = 0
while counter < 10:
    if counter == 5:
        counter += 1
        continue
    if counter == 8:
        break
    print(counter)
    counter +=1
else:
    print("Loop completed without break.")
 """

# Exercise 3: List Comprehension
""" numbers = list(range(21))
even_numbers = [num **2 for num in numbers if num % 2 == 0]
even_numbers_greater_ten = [num **2 for num in numbers if num % 2 == 0 and num > 10]
print("Squared even numbers:", even_numbers)
print("Squared even numbers, \nthat are greater than 10:", even_numbers_greater_ten)
 """
# Exercise 4: If-Elif-Else Decision Making
""" number = input("Enter a number between 0 and 100:")
try:
    number = int(number)
    
    if number > 100 or number < 0:
        print(f"Your number is: {number} Invalid Grade.")
    elif number >= 90:
        print(f"Your number is: {number} Score: Excellent.")
    elif number > 70 and number <= 89:
        print(f"Your number is: {number} Score: Good.")
    elif number > 50 and number <= 89:
        print(f"Your number is: {number} Score: Average.")
    else:
        print(f"Your number is: {number} Score: Fail.")        
    #print(number)

except ValueError:
    print("Invalid input. Please enter a number between 0 to 100.")
 """
# Exercise 5: Comparisons in a While Loop
""" secret_number = 7

while True: # Keep the while loop running until correct.
    # generate an input for the user with a question:
    num = input("Enter a number 0 to 10 to guess the correct one: \n")

    # catch the error with an try / except. 
    # if, elif and else should be inside the try.
    try:
        num = int(num) # converts the input to an integer

        if num < secret_number:
            print("Too low. Try again.")

        elif num > secret_number:
            print("Too high. Try again.")

        else:
            print("Correct! You got the secret number 7!")
            break
        
    # we are converting to an integer so we need a ValueError except.
    except ValueError:
        print("Invalid input. Please, enter a number.")
        
 """
# Exercise 6: Match-Case Statement

# First Version out of my head:
# Vending Machine
#selection
A = "A = Chips"
B = "B = Chocolate Bar"
C = "C = Soda"
D = "D = Candy"
option_D1 = "Candy with dip"
option_D2 = "Candy without dip"
E = "E = Sandwich"

items = A + ", " + B + ", " + C + ", \n" + D + ", " + E

print("Welcome to the vendor machine.")
print("Please make the following selection.")
print("Our current items to be sold are:")
print(items)

selection = input(" ") # ask the user to enter a selection from the vendor machine
selection = str(selection.upper()) # makes the input uppercase and type to string

try:
    print(f"\nPlease Choose: {selection}")
    match selection:
        case _ if selection == A:
            print("Chips dispensed.")
        case _ if selection == B:
            print("Chocolate Bar dispensed.")
        case _ if selection == C:
            print("Soda dispensed.")
        case _ if selection == D:
            print("Would you like extra dip with your candy? (Yes/No):")
        case _ if selection == E:
            print("Sandwich dispensed.")
        case _:
            print("Invalid selection, please try again.")
            
except ValueError:
    print("Invalid input, please enter from the presented item.") 

#final version (+45 min. later and looking up syntax)   
#selection
items = """
Product Selection:
A = Chips
B = Chocolate Bar
C = Soda
D = Candy
E = Sandwich"""

print("\n--- Welcome to the vendor machine ---")
print(items)

selection = input("\nSelect an item:").strip().upper() # ask the user to enter a selection from the vendor machine

try:
    match selection:
        case "A":
            print("Chips dispensed.")
        case "B":
            print("Chocolate Bar dispensed.")
        case "C":
            print("Soda dispensed.")
        case "D":
            extra_dip = input("Would you like extra dip with your candy? (Yes/No): ").strip().lower() # extra space to the input cursor is away one space
            if extra_dip == "yes":
                print("Candy with extra drip dispensed")
            else:
                print("Candy dispensed.")
        case "E":
            print("Sandwich dispensed.")
        case _:
            print("Invalid selection, please try again.")
            
except ValueError:
    print("Invalid input, please enter from the presented item.") 