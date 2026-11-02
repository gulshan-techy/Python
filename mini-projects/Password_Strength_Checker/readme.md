# 🔐 Password Strength Checker

## 📌 Overview

The Password Strength Checker is a beginner-friendly Python project that evaluates password strength based on different character types and password length.

It analyzes uppercase letters, lowercase letters, digits, and special characters to calculate a password strength score.

Based on the score, the program classifies the password as Weak, Medium, or Strong.

## ✨ Features

* Checks password length.
* Counts uppercase letters.
* Counts lowercase letters.
* Counts numeric digits.
* Counts special characters.
* Calculates a password strength score.
* Classifies passwords as Weak, Medium, or Strong.

## 🛠️ Python Concepts Used

| Concept                       | Purpose                              |
| ----------------------------- | ------------------------------------ |
| Import Module                 | Uses Python's string module          |
| Variables                     | Stores character counts and score    |
| For Loop                      | Iterates through password characters |
| If-Elif-Else                  | Identifies character types           |
| Conditional Statements        | Evaluates password strength          |
| String Methods and Properties | Analyzes password characters         |
| Comparison Operators          | Checks password requirements         |

## 💻 Source Code

```python
import string

print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

uppercase = 0
lowercase = 0
digits = 0
special_chars = 0

for char in password:

    if char in string.ascii_uppercase:
        uppercase += 1

    elif char in string.ascii_lowercase:
        lowercase += 1

    elif char in string.digits:
        digits += 1

    elif char in string.punctuation:
        special_chars += 1

score = 0

if len(password) >= 8:
    score += 1

if uppercase > 0:
    score += 1

if lowercase > 0:
    score += 1

if digits > 0:
    score += 1

if special_chars > 0:
    score += 1

print("\nPassword Analysis:")
print("Password Length:", len(password))
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special_chars)

print("\nPassword Strength:")

if score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")
```

## ▶️ How to Run

1. Make sure Python is installed.
2. Clone or download the repository.
3. Navigate to the `string-programs` directory.
4. Run the following command:

```bash
python password_strength_checker.py
```

## 📊 Password Strength Criteria

The program evaluates five conditions:

| Condition                                | Score |
| ---------------------------------------- | ----: |
| Password length is at least 8 characters |     1 |
| Contains uppercase letters               |     1 |
| Contains lowercase letters               |     1 |
| Contains digits                          |     1 |
| Contains special characters              |     1 |

### Strength Classification

| Score | Result |
| ----- | ------ |
| 0–2   | Weak   |
| 3–4   | Medium |
| 5     | Strong |

## 📚 Learning Outcome

Through this project, I practiced Python loops, conditional statements, string handling, module importing, character classification, and basic password validation logic.

## 🚀 Future Improvements

* Add minimum 12-character password recommendations.
* Detect common and easily guessable passwords.
* Check repeated characters and patterns.
* Add password visibility options.
* Implement more advanced password security checks.
