#code 1
# What happened in this line of code?
even_numbers = [number for number in range(10) if number % 2 == 0]
print("\nThis is 'even_numbers':", even_numbers)

#Code 2
# Start with an empty list to store even numbers
even_numbers_2 = []

# Loop through each number from 0 to 9 (range(10) generates numbers 0-9)
for number in range(10):  
    # Check if the number is even
    if number % 2 == 0:  
        # Add the even number to the list
        even_numbers_2.append(number)  

# Print the list of even numbers
print("\nThis is 'even_numbers_2':", even_numbers_2)


#Code 3
# Start with an empty list to store even numbers
even_numbers_3 = []

# Manually check and add even numbers from 0 to 9
if 0 % 2 == 0:
    even_numbers_3.append(0)
    print("\nThis is 'even_numbers_3', append(0):", even_numbers_3)

if 1 % 2 == 0:
    even_numbers_3.append(1)
    print("\nThis is 'even_numbers_3', append(1):", even_numbers_3)

if 2 % 2 == 0:
    even_numbers_3.append(2)
    print("\nThis is 'even_numbers_3', append(2):", even_numbers_3)

if 3 % 2 == 0:
    even_numbers_3.append(3)
    print("\nThis is 'even_numbers_3', append(3):", even_numbers_3)

if 4 % 2 == 0:
    even_numbers_3.append(4)
    print("\nThis is 'even_numbers_3', append(4):", even_numbers_3)

if 5 % 2 == 0:
    even_numbers_3.append(5)
    print("\nThis is 'even_numbers_3', append(5):", even_numbers_3)

if 6 % 2 == 0:
    even_numbers_3.append(6)
    print("\nThis is 'even_numbers_3', append(6):", even_numbers_3)

if 7 % 2 == 0:
    even_numbers_3.append(7)
    print("\nThis is 'even_numbers_3', append(7):", even_numbers_3)

if 8 % 2 == 0:
    even_numbers_3.append(8)
    print("\nThis is 'even_numbers_3', append(8):", even_numbers_3)

if 9 % 2 == 0:
    even_numbers_3.append(9)
    print("\nThis is 'even_numbers_3', append(9):", even_numbers_3)

# Print the list of even numbers
print("\nThis is 'even_numbers_3':", even_numbers_3)