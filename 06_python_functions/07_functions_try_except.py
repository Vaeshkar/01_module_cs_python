def divide_10_by_n(number):
    try:
        result = 10 / number
    except TypeError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"10 divided by {number} is {result}.")
    finally:
        print("Execution of try...except block is complete.\n")
        
divide_10_by_n('hi')
divide_10_by_n(0)
divide_10_by_n(2)
divide_10_by_n(3)