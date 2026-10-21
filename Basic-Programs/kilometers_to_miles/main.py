# Program to convert kilometers to miles

# 1 kilometer = 0.621371 miles

km = float(input("Enter distance in kilometers: "))

if km < 0:
print("Distance cannot be negative.")
else:
miles = km * 0.621371
print(f"{km:.2f} kilometers is equal to {miles:.2f} miles.")
