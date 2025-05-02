# Simple case
day_number = 3

match day_number:
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
  case _:
    print("Weekend or an invalid day number")

# Using pattern matching with more complex data,
# for example a set of coordinates
#point = (0, 0)
#point = (1, 0)
#point = (0, 1)
point = (1, 2)

match point:
  case (0,0):
    print("Point is at the origin.")
  case (0,y):
    print(f"Point is on the y-axis at y={y}.")
  case (x,0):
    print(f"Point is on the x-axis at x={x}.")
  case (x,y):
    print(f"Point is at coordinates at x={x}, y={y}.")
    