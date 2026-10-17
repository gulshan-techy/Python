# 🐍 Sum of Natural Numbers Using a For Loop

## 📌 About the Project

This Python program calculates the sum of natural numbers from `1` up to a number entered by the user.

It uses a `for` loop to iterate through the numbers and an accumulator variable to calculate the total.

## 🎯 Concepts Covered

- `input()` — Accepting user input.
- `int()` — Converting input into an integer.
- `range()` — Generating a sequence of numbers.
- `for` loop — Iterating through the sequence.
- Accumulator variable — Maintaining a running total.
- `+=` operator — Adding each number to the total.
- `print()` — Displaying the final result.

## 💻 Python Code

```python
num = int(input("Enter a number here: "))

total = 0

for i in range(1, num + 1):
    total += i

print("Sum of natural numbers:", total)
```

## ▶️ Sample Output

**Example 1:**

```
Enter a number here: 5
Sum of natural numbers: 15
```

**Example 2:**

```
Enter a number here: 10
Sum of natural numbers: 55
```

## ⚙️ How to Run

Make sure Python 3 is installed on your system.

Run the following command from the directory containing the file:

```
python sum_of_natural_numbers.py
```

Depending on your system, use `python3` instead of `python` if required.

## 📚 What I Learned

- How to use a `for` loop to iterate over a range.
- How to calculate a running total using an accumulator.
- How `range(1, num + 1)` includes the final number.
- How to use the `+=` assignment operator.
- How to solve a basic mathematical problem using programming logic.

## 🚀 Learning Journey

This program is part of my Python fundamentals practice. I am building a strong programming foundation to support my learning journey in Cloud Computing, DevOps, and Automation.

**Learning Python one program at a time!** 🐍
