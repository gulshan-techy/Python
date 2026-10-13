# 🐍 Day 20: 'is' vs '==' in Python

## 📌 Overview
Have you ever compared two variables in Python, noticed they have the exact same value, but wondered why choosing between `==` and `is` gives different results? 

Today, I explored the exact difference between **`==` (equality operator)** and **`is` (identity operator)**, and how Python manages objects under the hood in memory!

---

## 🛠️ Concepts Learned

### 1. Value Equality (`==`) vs. Memory Identity (`is`)
*   **`==` (Value Equality):** Checks whether the **values** inside two objects are equal. (Do they contain the same data?)
*   **`is` (Identity Operator):** Checks whether two variables point to the **exact same physical location in memory** (RAM address).

Think of it like buying two identical smartphones. They have the exact same model and features (`==` is True), but they are two physically separate phones (`is` is False).

### 2. Example with Lists (Mutable Objects)
```
# Two separate lists with identical values
a = [1, 2, 3]
b = [1, 2, 3]

# Values are the same
print(a == b)  # Output: True

# Memory locations are different (Two separate list objects in RAM)
print(a is b)  # Output: False
```

### 3. Python Optimization & Immutable Objects
Why does is sometimes return True for numbers or short strings even if we create them separately?
Because Python is smart! For immutable objects (like numbers, strings, or tuples) that don't change, Python reuses the same memory location to save space.

```
x = 3
y = 3

# Here, both value and memory location match because Python optimizes small integers
print(x == y)  # Output: True
print(x is y)  # Output: True
```
### 4. Working with None
The is operator is most commonly used in Python when checking for None. Because there is only ever one None object in Python's memory, checking variable is None is the standard best practice.

```
user_status = None

if user_status is None:
    print("User is not logged in.")
```

### 💡 Summary
Use == when you want to check if two variables have the same value.

Use is when you want to check if two variables refer to the exact same object in memory (especially when checking for None).
