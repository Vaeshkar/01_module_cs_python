# 1. Sum of List Elements
# def sum_list(numbers: list):
#     total = 0
#     for num in numbers:
#         print(f"current num is: {num}")
#         total += num
#         print(f"current total is: {total}")
#     return total
    
# print(sum_list([5, 6, 4, 3]))


# 2. Repeated Greeting

# def repeat_greeting(name, times):
#     for greet in range(times, 0, -1 ):
#         print(f"Hello {name}! ({greet} left)")
#     return "All your greetings are printed." # set so we don't get an empty None return from the func    
  
# result = repeat_greeting("Dennis", 5)  
        
# print(result)

# 3. Factorial Calculation

# def factorial(n):
#     factorial_num = 1
#     for num in range(1, n + 1):
#         factorial_num *= num
#     return factorial_num

# n = 5 # stores the argument value
# number = factorial(n) # takes the n from the variable
# # print(factorial(6)) # test to see if the n var gets updated. Result: I loop two times. 1st the n_5 and 2nd the n_6.
# print(f"The factorial number of {n} is {number}.") # can print out the {n} and the {number}

# 4. Fibonacci Sequence Generator

# def fibonacci(n):
#     # generate a starting list with 0 and 1
#     fibo_list = [0,1]

#     # A mini except.
#     # checks if the user wants a number that is not working with the sequence.  
#     if n == 1 or n == 0:
#         return f"Warning: Value is too low. \nEntered number: {n}. Need a minimal of 2."
    
#     # loop with the i (index) over the range of n and start after the index 0 and 1. These are given. 
#     for i in range(2, n):
#         # create a var and add sum the two indexes from the fibo_list position last -1 and second last -2
#         next_fibo_num = fibo_list[-1] + fibo_list[-2]
#         # add the new number to the fibo_list so the next F(n) can iterate until the n value is reached
#         fibo_list.append(next_fibo_num)
#     # return the final list [] to the console/terminal
#     return fibo_list

# print(fibonacci(8))

# test loop
# def recursive_sum(lst, index=0):
#     if index == len(lst):
#         return 0
#     return lst[index] + recursive_sum(lst, index + 1)

# print(recursive_sum([1,2,3]))

# def get_sum_of_digits(num:int):
#     sum = 0
#     digits = list(str(num)) # convert the numbers to str, so it is iterable
#     print(digits)
#     for x in digits:
#         sum += int(x) # convert the str back to numbers so we can add up the numbers.
#     return sum

# print(get_sum_of_digits(123))

# def get_product_of_digits(num):
#     result = 0
#     digits = list(str(num))
#     for x in digits:
#         result *= int(x)
#     return result

# print(get_product_of_digits(123))

# def count_even_digits(num):
#     result = []
#     digits = list(str(num))
#     for x in digits:
#         if int(x) % 2 == 0: # get the even numbers
#             result.append(x)
#     #print(digits)    
#     return result
    
# print(count_even_digits(123456))
# print()
# print(count_even_digits(141516171819))
# print()
# print(count_even_digits(789))
# print()
# print(count_even_digits(24680))
# print()
# print(count_even_digits(13579))
# print()

a, b, c = (5, 10, 15)
print(b)

x = True
y = False
print(x and not y)

nums = [1, 2, 3, 4, 5]
new_list = [x**2 for x in nums if x % 2 == 0]
print(new_list)

count = 0

while count < 5:
    print(count)
    if count == 2:
        break
    count += 1
    
""" def add(x, y):
    return x + y

print(add(3, "4")) """

nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[1:6:2])

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)

def my_func():
    return 1, 2, 3

x, y, z = my_func()
print(y)

