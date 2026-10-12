# 🐍 Day 19: Match Case Statements in Python

## 📌 Overview
If you have ever written a long chain of `if-elif-else` statements just to check a single variable against multiple possible values, you know how messy your code can get. 

Starting from Python 3.10, Python introduced a powerful new feature to solve this: **Match Case Statements** (similar to `switch-case` statements in languages like C, C++, and Java). Today, I learned how to use `match` and `case` to make conditional code cleaner and much more readable!

---

## 🛠️ Concepts Learned

### 1. What is a Match Case?
A match statement compares a variable's value against different patterns (cases). When it finds a match, it executes the corresponding block of code.

### 2. Basic Syntax & Example
Here is how a basic match-case statement works in Python:

```
x = int(input("Enter the value of x: "))

# Match the value of x against different cases
match x:
    # If x is 0
    case 0:
        print("x is zero")
    
    # If x is 4
    case 4:
        print("case is four")
```

### 3. The Default Case (_)
Just like the else block at the end of an if-elif chain, the underscore (_) acts as a wildcard or default case. If none of the specific cases match the variable, Python automatically falls back to the case _: block.

### 4. Python vs. Other Languages (No break needed!)
If you are coming from languages like C++ or Java, you might be used to writing a break statement at the end of every case so the program doesn't accidentally run the next case.

In Python, you don't need break!

Once a matching case is found and executed, Python automatically exits the match block. It won't "fall through" to the other cases.

### 5. Adding if Conditions (Guards) inside Cases
You can make your cases even smarter by attaching an if condition right next to the pattern:

```
x = 55

match x:
    case _ if x != 90:
        print(f"{x} is not 90")
    case _ if x != 80:
        print(f"{x} is not 80")
    case _:
        print("Default case")
```
    # Default case if nothing else matches (using underscore)
    case _:
        print("x is:", x)
