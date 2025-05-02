# 1. Simple While Loop
print("Simple While Loop:")
count = 1
while count <= 5:
  print("Count:", count)
  count += 1
else:
  print("Simple loop finished.\n")
  
# 2. While Loop with continue (starting count at 1)
print("While Loop with 'continue' (skipping even numbers):")
count = 0
while count < 10:
  count += 1
  if count % 2 == 0:
    continue # skip printing for even numbers
  print("Off number:", count)
print("Finished skipping even numbers.\n")

# 3. While Loop with break and else
print("While Loop with 'break'")
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
else:
  print("This won't be executed")
  
print("Search completed.")