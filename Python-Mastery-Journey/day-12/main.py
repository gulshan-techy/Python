print(" 🚀 Day 12 Practice: Exception Handling (Try-Except)")
# 1.  Basic Try-Except (Preventing a Crash)
print("---------------------------------------------------------")
print("1. Basic Error Handling:")
try:
    print(" Attempting to divide 10 by 0...")
    result = 10 / 0  # This will cause a ZeroDivisionError
except:
    print(" ❌ Error caught! You cannot divide by zero.")

# 2.  Catching the Exact Error Message (Exception as e)
print("---------------------------------------------------------")
print(" 2.  Printing the Actual Error Message:")
try:
    print(" Attempting to convert the word 'Hello' into a number...")
    bad_number = int("Hello")  # This will cause a ValueError
except Exception as e:
    print(f" ⚠️ Caught an Exception: {e}")

# 3.  Handling Multiple Specific Errors
print("---------------------------------------------------------")
print(" 3.  Handling Specific Errors (IndexError):")
my_list = ["Apple", "Banana", "Cherry"]
try:
    print(" Accessing the 5th item in a 3-item list...")
    print(my_list[5])  # This will cause an IndexError
except ValueError:
    print(" ❌ ValueError: Invalid value.")
except IndexError:
    print(" ❌ IndexError caught! That item does not exist in the list.")

print(" 🎉 Program finished successfully without crashing!")
