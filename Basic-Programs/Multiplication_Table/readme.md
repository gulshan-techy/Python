# 🐍 Multiplication Table Program in Python

## 📌 About the Project

This is a beginner-friendly Python program that prints the multiplication table of a number entered by the user.

The program uses a `for` loop to iterate from 1 to 10 and calculates each multiplication result.

## 🎯 Concepts Covered

- `input()` — Taking input from the user.
- `int()` — Converting user input into an integer.
- `for` loop — Repeating instructions for a sequence of values.
- `range()` — Generating numbers from 1 to 10.
- `*` operator — Performing multiplication.
- f-strings — Formatting output in a readable way.

## 💻 Python Code

```
# Multiplication Table Program

num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

## ▶️ Sample Output

```
Enter a number: 5
Multiplication Table of 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

## ⚙️ How to Run

Make sure Python 3 is installed on your system.

Run the following command from the directory containing the Python file:

```
python multiplication_table.py
```

Depending on your system, use `python3` instead of `python` if required.

## 📚 What I Learned

- How to generate a multiplication table using a loop.
- How the `range()` function controls loop iterations.
- How to use the multiplication operator.
- How to format output using f-strings.
- How to identify and correct a Python syntax error.

## 🚀 Learning Journey

This program is part of my Python fundamentals practice. I am strengthening my programming logic and problem-solving skills as I work toward my goals in Cloud Computing, DevOps, and Automation.

**Learning Python one program at a time!** 🐍
