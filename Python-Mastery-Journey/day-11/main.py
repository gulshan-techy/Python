# 1. Default Arguments
print(" Default Arguments:")
def greet_user(name, greeting="Hello"):
    print(f" {greeting}, {name}!")

greet_user("Gulshan")  # Uses default greeting
greet_user("Gulshan", "Good Morning")  # Overrides default
print("----------------------------------------------")

# 2. Keyword Arguments
print(" Keyword Arguments (Order doesn't matter):")
def print_profile(first_name, last_name):
    print(f" Profile: {first_name} {last_name}")

# Passing arguments by name in reverse order
print_profile(last_name="Kumar", first_name="Gulshan")
print("----------------------------------------------")

# 3.  Variable-Length Arguments (*args) & Return Statement
print("\n *args and Return Statement:")
def calculate_average(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average  # Returning the value instead of printing!

# Storing the returned value in variables
result1 = calculate_average(10, 20, 30)
result2 = calculate_average(5, 7, 9, 11, 15)

print(f" Average of (10, 20, 30) is: {result1}")
print(f" Average of (5, 7, 9, 11, 15) is: {result2}")

