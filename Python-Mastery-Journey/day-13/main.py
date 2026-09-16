print(" 🚀 Day 13 Practice: The 'finally' Keyword")
# 1.  Basic Try-Except-Finally (Error Simulation)
print("1.  Basic Try-Except-Finally:")
try:
    print("Attempting to divide 10 by 0...")
    result = 10 / 0
except ZeroDivisionError:
    print("Error caught! Division by zero is not allowed.")
finally:
    print("FINALLY BLOCK: This will always execute (Cleaning up...)")

# 2. The True Power of 'finally' (Inside a Function with Return)
print("2. The True Power of 'finally' (Inside a Function):")
def fetch_data():
    try:
        print("Opening file to read data...")
        # Simulating a successful read and returning immediately
        return "Success: Data Fetched"
        
    except Exception as e:
        print("Error occurred.")
        return " Failed"
        
    finally:
        # This executes BEFORE the function actually returns the value!
        print("FINALLY BLOCK: Closing the file (Executes before return!)")

# Call the function and store the result
output = fetch_data()

# Print the value that the function returned
print(f"Function ultimately returned: {output}")
