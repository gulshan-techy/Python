# 🐍 Find the Greatest of Three Numbers in Python

## 📌 About the Project

This is a beginner-friendly Python program that finds the greatest value among three numbers entered by the user.

The program uses conditional statements (`if`, `elif`, and `else`) along with the logical operator `and` to compare the three numbers.

## 🎯 Concepts Covered

* `input()` — Accepting input from the user.
* `int()` — Converting input into integers.
* Variables — Storing values in variables.
* `if-elif-else` — Implementing decision-making logic.
* Comparison operators — Using `>=` to compare values.
* Logical operator `and` — Combining multiple conditions.

## 💻 Python Code

```
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is greatest")

elif num2 >= num1 and num2 >= num3:
    print(num2, "is greatest")

else:
    print(num3, "is greatest")
```

## ▶️ Sample Output

**Example 1: Different numbers**

```text
Enter first number: 10
Enter second number: 25
Enter third number: 15
25 is greatest
```

**Example 2: Two equal greatest numbers**

```
Enter first number: 10
Enter second number: 10
Enter third number: 5
10 is greatest
```

**Example 3: All numbers equal**

```text
Enter first number: 7
Enter second number: 7
Enter third number: 7
7 is greatest
```

## ⚙️ How to Run

Make sure Python 3 is installed on your system.

Run the following command from the directory containing the Python file:

```
python greatest_of_three_numbers.py
```

Depending on your system, you may need to use `python3` instead of `python`.

## 📚 What I Learned

* How to take multiple inputs from a user.
* How to compare three numbers using conditional statements.
* How to combine conditions using the `and` operator.
* How comparison operators affect program logic.
* How to handle equal values correctly.

## 🚀 Learning Journey

This program is part of my Python fundamentals practice. I am strengthening my programming logic and problem-solving skills as I work toward my goals in Cloud Computing, DevOps, and Automation.

**Learning Python one program at a time!** 🐍
