# 🐍 Day 15: Variable Scope (Local, Global) & Constants

## 📌 Overview
Imagine your Python script is a house. Some things are kept in the living room for everyone to see, while other things are locked inside a private bedroom. 

In Python, this concept is called **Scope**. Scope determines where a variable can be seen, used, or changed. Today, I took a deep dive into **Local Variables, Global Variables**, and the concept of **Constants** in Python.

---

## 🛠️ Concepts Learned (In Detail)

### 1. Local Variables (The Private Room)
A Local Variable is created *inside* a function. It belongs ONLY to that function. 
*   **Birth:** It is created when the function starts.
*   **Death:** It is destroyed the moment the function finishes executing.
*   **Rule:** You cannot access a local variable from outside its function.

```
def my_function():
    # This is a LOCAL variable
    secret_code = 1234
    print("Inside the function, I know the code is:", secret_code)

my_function()

# ❌ ERROR: Python doesn't know what 'secret_code' is outside the function!
# print(secret_code)  # This will throw a NameError
```

### 2. Global Variables (The Public Billboard)
A Global Variable is created outside of any function (usually at the very top of your script).

Birth: Created when the script starts.

Rule: Because it is global, every function inside your script can read it.

```
# This is a GLOBAL variable
player_name = "Gulshan"

def greet_player():
    # The function can easily read the global variable
    print("Welcome back,", player_name)

def start_game():
    # This function can also read it!
    print(player_name, "is starting the game...")

greet_player()
start_game()
```

### 3. The global Keyword (Modifying Global from Local)
Here is a tricky part: A function can read a global variable, but it cannot change it by default. If you try to change it, Python will just create a new, temporary local variable with the same name.

To actually change a global variable from inside a function, you must use the global keyword.

```
score = 0  # Global variable

def increase_score():
    # Tell Python: "I want to modify the GLOBAL score, don't create a new one!"
    global score
    score = score + 10
    print("Score inside function:", score)

increase_score()
print("Score outside function:", score)  # Output will be 10
```

### 4. Constants (The "Do Not Touch" Variables)
In languages like C++ or Java, you can lock a variable so its value can never be changed.
Python does NOT have true constants.

However, Python programmers use a very strict naming convention to simulate constants: ALL_CAPS. When you write a variable name in all uppercase letters, it is a signal to other developers (and yourself) saying: "This is a constant. Do not change its value!"

```
# Constants are written in ALL CAPS
PI = 3.14159
MAX_USERS = 100
WEBSITE_URL = "[https://gulshanai.online](https://gulshanai.online)"

def calculate_area(radius):
    # We read the constant, but we NEVER try to change it
    area = PI * (radius * radius)
    print("Area is:", area)

calculate_area(5)
```
