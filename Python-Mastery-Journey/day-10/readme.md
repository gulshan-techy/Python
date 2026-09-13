# 🐍 Day 10: Functions in Python (Part 1)

## 📌 Overview
Writing the same logic 50 times in a program is not just boring, it's inefficient. If you make a mistake, you'd have to go back and fix it in 50 different places! 

To solve this problem, Python provides **Functions**. A function is a block of code that performs a specific task. You write the code once, wrap it in a function, and then "call" it wherever and whenever you need it.

---

## 🛠️ Concepts Learned

### 1. Creating a Basic Function
To define a function in Python, we use the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. 

```
# Defining the function
def calculate_gmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

# Calling the function
calculate_gmean(9, 8)
calculate_gmean(8, 7)

Why this is useful: Instead of writing the mathematical formula over and over again for different pairs of numbers, we just type calculate_gmean() and pass the numbers to it.
```

### 2. Passing Arguments to Functions
Functions act like customized mini-programs. You can give them inputs (called arguments or parameters) to work with.

```
# A function that takes two arguments (a and b) and compares them
def is_greater(a, b):
    if a > b:
        print("First number is greater")
    elif a == b:
        print("Both numbers are equal")
    else:
        print("Second number is greater")

# Reusing the logic for different values
is_greater(10, 20)  # Output: Second number is greater
is_greater(50, 10)  # Output: First number is greater

```

### 3. The pass Keyword
Sometimes, when you are building a large program, you know you will need a function (e.g., is_lesser), but you don't want to write its logic immediately.

If you just leave a function empty, Python will throw an IndentationError. To prevent this, you use the pass keyword. It tells Python to "skip this for now and keep running the rest of the code."

```
def is_lesser(a, b):
    pass  # I will write the logic for this later. Python will ignore this and not throw an error.

print("Program continues to run successfully!")
```

### 4. Built-in vs. User-Defined Functions
Built-in Functions: These are ready-made functions provided by Python. You don't need to define them. Examples: print(), len(), min(), max(), sum(), range().

User-Defined Functions: These are the custom functions that we create using the def keyword to perform specific tasks for our own programs (like the is_greater() function we built above).
