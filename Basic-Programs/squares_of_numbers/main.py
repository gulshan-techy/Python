num = int(input("How many squares do you want? "))

if num <= 0:
  print("Please enter a positive number.")
else:
  for i in range(1, num + 1):
    print(f"{i} * {i} = {i * i}")
