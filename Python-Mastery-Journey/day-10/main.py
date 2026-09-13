# 1️. Basic Function
print("1. Basic Function Call:")
def greet_user(name):
    print(f" Hello, {name}! Welcome to Day 10.")

greet_user("Gulshan")
greet_user("Network")
print("--------------------------------------------------")

# 2. Function with Logic (Arguments)
print("2. Function with Conditional Logic:")
def compare_numbers(a, b):
    if a > b:
        print(f" {a} is greater than {b}")
    elif a == b:
        print(f" Both numbers are equal ({a})")
    else:
        print(f" {b} is greater than {a}")

compare_numbers(10, 20)
compare_numbers(50, 10)
print("--------------------------------------------------")

# 3. The 'pass' keyword
print("3. Using the 'pass' keyword:")
def advanced_logic_coming_soon():
    pass  # Python ignores this empty function safely

print(" function called successfully without crashing!")
