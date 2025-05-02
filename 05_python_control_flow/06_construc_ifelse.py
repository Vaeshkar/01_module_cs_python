# Simple 'if'
number = 10
if number > 5:
  print("Number is greater than 5.")
  
# 'if' ... 'else' example
if number % 2: #division of 2
  print("Number is odd.")
else:
  print("Number is even.")
  
# 'if' 'elif' else' example
score = 85
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade B")
elif score >= 70:
  print("Grade C")
else:
  print("Grade: D or below")
  
# Shorthand 'if' 'else' (ternary operator) example
result = 'odd' if number % 2 else 'even' 
print("The number is", result) # In a Ternary don't indent the print. 

# The following block will throw an error if uncommented
if number > 0:
  print ("Positiv number")