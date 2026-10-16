# 🐍 Finding the Exact Integer Square Root in Python

## 📌 About the Project

This Python program finds the exact integer square root of a non-negative integer using a `for` loop and a conditional statement.

It checks whether the square of an integer is equal to the given number. If a match is found, the program displays the square root. Otherwise, it reports that no exact integer square root was found.

## 🎯 Concepts Covered

- `input()` — Accepting user input.
- `int()` — Converting input into an integer.
- `if-else` — Handling conditions.
- `for` loop — Checking possible integer values.
- `break` — Stopping the loop when a match is found.
- `for-else` — Handling the case where no match is found.
- Arithmetic operators — Using multiplication to check perfect squares.

## 💻 Python Code

```
num = int(input("Enter a number to find the square root: "))

if num < 0:
    print("Square root of negative numbers is not defined in real numbers.")
else:
    for i in range(num + 1):
        if i * i == num:
            print("Square root of", num, "is:", i)
            break
    else:
        print("No exact integer square root found for", num)
```

## ▶️ Sample Output

**Example 1: Perfect square**

```
Enter a number to find the square root: 25
Square root of 25 is: 5
```

**Example 2: Not a perfect square**

```text
Enter a number to find the square root: 20
No exact integer square root found for 20
```

**Example 3: Zero**

```
Enter a number to find the square root: 0
Square root of 0 is: 0
```

## ⚙️ How to Run

Make sure Python 3 is installed, open a terminal in the `loops` directory, and execute:

```
python exact_square_root.py
```

Depending on your system, use `python3` if necessary.

## 📚 What I Learned

- Using loops to solve mathematical problems.
- Checking perfect squares with multiplication.
- Using `break` to exit a loop.
- Understanding Python's `for-else` construct.
- Handling zero and negative inputs.
- Improving code by removing unnecessary nested loops.

## 🚀 Learning Journey

This program is part of my Python fundamentals practice. I am strengthening my programming logic and problem-solving skills as I work toward my goals in Cloud Computing, DevOps, and Automation.

**Learning Python one program at a time!** 🐍
