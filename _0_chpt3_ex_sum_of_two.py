################
# Sum of Two

## GOAL ##
# find the INDEX of 2 elements in nums whose SUM is equal to target
# you cannot use the same element twice
# there is always one valid solution

# func = sum_of_two
# var1 = nums
# var2 = target

# O(n^2) Version
def sum_of_two(nums: list, target: int):
    i = 1 # index counter for the loops
    
    for n in nums:
        for m in nums[i:]:
            if n + m == target:
                index_of_n = nums.index(n)
                index_of_m = nums.index(m, index_of_n + 1)
                return [index_of_n, index_of_m]

# create a list of numbers
nums = [5, 7, 3, 5, 8, 9, 10, 12, 15, 17, 13, 20, 40]

# create a target number
target = 10

print(sum_of_two(nums, target))

# O(n) Version
def sum_of_two(nums, target):
    # create a dict called complement(set of pairs) to store the keys: 'number' and values: 'index'
    complement = {}
    
    for i, num in enumerate(nums):
        need_number = target - nums[i]

        if need_number in complement:
            return [complement[need_number], i]
        
        complement[num] = i


# create a list of numbers
nums = [5, 7, 3, 5, 8, 9, 10, 12, 15, 17, 13, 20, 40]

# create a target number
target = 10

print(sum_of_two(nums, target))


# Two Product Problem

# def two_product_problem(nums, target):
#     #create a dict
#     complement = {}
#     # iterate true the nums list and set index and numbers with enumerate() function
#     for i, num in enumerate(nums):
#         # check if the needed_number is our target divided by nums index
#         number_need = target // nums[i]
        
#         if number_need in complement:
#             return [complement[number_need], i]
        
#         # if 
#         complement[num] = i
    
# # create a list of numbers
# nums = [5, 7, 3, 5, 8, 9, 10, 12, 15, 17, 13, 20, 40]
# # create a target number
# target = 21

# print(two_product_problem(nums, target))


# Two Sum II – Input Array is Sorted _ O(n) Complexity

# def two_sum_2(numbers, target):
    
#     # define the starter numbers. 
#     # create two variables with the index of left[0] and right[-1, meaning last]
#     left, right = 0, len(numbers) -1
    
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         # check if the curent_sum is equal to the target
#         if current_sum == target:
#             # If so, return both left and right number and add +1 index to them
#             return [left + 1, right + 1]
#         # check if the current_sum is less then the target
#         elif current_sum < target:
#             left += 1 # move the left numbers on index to the right
#         else:
#             right -= 1 # move the right numbers one index to the left
    
#     # If no solution is found, stop the loop and return an empty list.
#     return [] 

# # create a list 
# numbers = [2, 7, 11, 15]
# # create a target number
# target = 9

# # call the function
# print(two_sum_2(numbers, target))

