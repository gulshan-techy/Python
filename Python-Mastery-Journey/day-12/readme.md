# 🐍 Day 12: Exception Handling in Python

## 📌 Overview
Sometimes, the code we write runs into errors. This could be because a user typed a word instead of a number, or a server we are trying to reach is down. 

When Python encounters an error, it completely **halts and crashes the program**. None of the code below the error will execute. To prevent our program from crashing and to handle these errors gracefully, we use **Exception Handling** (`try` and `except`).

---

## 🛠️ Concepts Learned

### 1. The Problem: Why Programs Crash
If a program asks for an integer but the user types a string (like a name), Python doesn't know how to multiply it. It throws a `ValueError` and the program stops immediately.

```
# ❌ DANGEROUS CODE
a = input("Enter a number: ")
a = int(a)  # If the user types "Harry", the program crashes right here!

print("Multiplication table of", a)
for i in range(1, 11):
    print(a * i)

# This line will NEVER run if there is an error above
print("Some important lines of code at the end.")
```

### 2. The Solution: try and except
We can wrap the risky code inside a try block. If an error happens, instead of crashing, Python will jump to the except block and continue running the rest of the program!
```
# ✅ SAFE CODE
a = input("Enter a number: ")

try:
    a = int(a)
    print("Multiplication table of", a)
    for i in range(1, 11):
        print(a * i)
except:
    print("Invalid Input! You did not enter a valid number.")

# This line WILL run, even if the user typed text instead of a number!
print("End of program. We successfully avoided a crash.")
```
### 3. Finding out exactly what went wrong
Sometimes, you want to see the actual error message that Python threw without crashing the program. You can do this using Exception as e.
```
try:
    num = int(input("Enter an integer: "))
except Exception as e:
    print("Sorry, an error occurred. The error is:", e)
```
### 4. Handling Specific Errors
A single block of code might have different types of errors. For example, a user might enter invalid text (ValueError), or they might try to access a list item that doesn't exist (IndexError). We can handle these separately using multiple except blocks.

```
try:
    num = int(input("Enter an index to fetch from the list: "))
    my_list = [6, 3, 2]
    
    print("The value is:", my_list[num])

except ValueError:
    print("Error: The number entered is not an integer.")
    
except IndexError:
    print("Error: The index is out of bounds for the list.")
```

How it works:
- If the user types "hello", the ValueError block runs.
- If the user types "10" (but the list only has 3 items), the IndexError block runs.
