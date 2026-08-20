# Python Practice: User Input & Typecasting

print("--------------------------------------------------")
print("1️⃣ Basic User Input")
print("--------------------------------------------------")
name = input("Enter your name: ")
print("Hello", name, "! Welcome to Python practice.\n")


print("--------------------------------------------------")
print("2️⃣ The String Trap & Explicit Typecasting")
print("--------------------------------------------------")
# Taking input from user
num1 = input("Enter first number (e.g., 12): ")
num2 = input("Enter second number (e.g., 100): ")

# Without typecasting (Python treats them as strings)
wrong_result = num1 + num2
print("❌ Without Typecasting (Concatenation):", wrong_result)

# With explicit typecasting (Converting string to integer)
correct_result = int(num1) + int(num2)
print("✅ With Typecasting (Actual Addition):", correct_result, "\n")


print("--------------------------------------------------")
print("3️⃣ Implicit Typecasting (Automatic)")
print("--------------------------------------------------")
integer_value = 8       # int
float_value = 1.9       # float

# Python automatically converts the integer to a float to prevent data loss
final_value = integer_value + float_value
print(f"Adding int ({integer_value}) and float ({float_value}).")
print("Result:", final_value)
print("Data Type of Result:", type(final_value), "\n")


print("--------------------------------------------------")
print("4️⃣ Bonus: User Input for Automation Scripts")
print("--------------------------------------------------")
# Practical example: Asking for confirmation
action = input("Do you want to STOP the EC2 Instance? (yes/no): ")

# .lower() makes sure "YES", "Yes", and "yes" are all treated the same
if action.lower() == "yes":
    print("Stopping the server... 🛑")
else:
    print("Action canceled. ✅\n")

print("Practice script finished successfully! 🎉")
