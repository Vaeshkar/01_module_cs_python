# Using else and finally
# try:
#     number = int("123")  # Successful conversion
# except ValueError:
#     print("Error: Invalid number.")
# else:
#     print(f"Conversion successful! The number is {number}.")
# finally:
#     print("This block always runs, whether there was an error or not.")


# Real-world example: handling user input
# user_input = input("Enter an integer: ")

# try:
#     number = int(user_input)
#     result = number  # If conversion is successful, result will store the integer
# except ValueError:
#     result = "Invalid input: Please enter a valid integer."

# print(result)

# Real-world example 2: Process order discount
# def process_order_discount_real(user_input):
#     """
#     Process the discount rate for an order with robust error handling.
#     In a production environment, errors would be logged rather than printed.
#     """
#     try:
#         discount_rate = 100 / int(user_input)
#     except (ValueError, ZeroDivisionError) as e:
#         # Log the error using your logging framework, e.g., logging.error(f"...")
#         print(f"Error processing discount rate: {e}")  # For demonstration only.
#         discount_rate = None
#     except Exception as e:
#         # Catch-all for any other unexpected errors.
#         print(f"Unexpected error: {e}")  # For demonstration only.
#         discount_rate = None
#     else:
#         print(f"Discount rate computed successfully: {discount_rate}")  # For demonstration only.
#     finally:
#         print("Cleanup actions completed.")  # For demonstration only.
    
#     return discount_rate

# # Example usage (for demonstration):
# print(process_order_discount_real("50")) # Expected valid computation.
# print()
# print(process_order_discount_real("0"))    # Expected to catch ZeroDivisionError.
# print()
# print(process_order_discount_real("invalid"))  # Expected to catch ValueError.


# 1. Input conversion with try...except
# result = None
# while result is None:
#     user_input = input("Enter an integer (number): ")
    
#     try:
#         number = int(user_input)
#         result = number
#     except (ValueError):
#         print(f"Invalid input: {user_input} is not a number. Try again.")
    
# print(f"The number you entered is: {result}.")

# 2. Division with error handling

# def save_divide(dividend, divisor):
#     try:
#         result = dividend / divisor
#         return result    
#     except (ZeroDivisionError):
#         return ("Error: Division by zero.")
#     except (TypeError):
#         return ("Error: Invalid input types. Please use numbers.")
#     except (Exception) as e:
#         return (f"Unexpected Error: {e}")

    

# print(save_divide(4,0)) # Error test, division by zero.
# print(save_divide(10,5)) # should result in 2
# print(save_divide("a", "b"))

# 3. Dictionary key lookup

def get_value(dictionary, key):
    try:
        if not isinstance(key, str):
            return f"Error: {key} is not a valid key. Expected a string."
        return dictionary[key]  
      
    except KeyError:
        return "Error: Key not found in dictionary."
    
    except Exception as e:
        return f"Unexpected Error: {e}."

my_dict = {"apple": 5, "banana": 7, "orange": 12}

print(get_value(my_dict, "apple")) # return key value 5
print(get_value(my_dict, "orange")) # returns key value 12
print(get_value(my_dict, "pear")) # test except: KeyError
print(get_value(my_dict, 123)) # test except: Exception error, will trow the 1st error in try. 