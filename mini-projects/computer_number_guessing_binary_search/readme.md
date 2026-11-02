# 🧠 Computer Number Guessing Game Using Binary Search

## 📌 Overview

This is a Python-based Computer Number Guessing Game that uses the Binary Search Algorithm.

Unlike a traditional number guessing game where the user guesses the computer's number, in this game the computer tries to guess the number selected by the user.

The user thinks of a number between 1 and 100 and provides hints such as "higher", "lower", or "correct".

The computer uses Binary Search to eliminate half of the remaining possibilities after each guess, allowing it to identify the correct number in a maximum of 7 attempts.

## ✨ Features

* Computer guesses the number selected by the user.
* Uses the Binary Search Algorithm.
* Searches within a range of 1 to 100.
* Finds the middle number using integer division.
* Updates the search range based on user feedback.
* Provides a maximum of 7 attempts.
* Handles uppercase and lowercase inputs.
* Detects inconsistent user responses.
* Displays the total attempts taken to guess the number.

## 🛠️ Python Concepts Used

| Concept                 | Purpose                                        |
| ----------------------- | ---------------------------------------------- |
| Variables               | Stores the minimum and maximum search range    |
| Binary Search           | Efficiently narrows down the possible numbers  |
| `for` Loop              | Controls the maximum number of attempts        |
| `if-elif-else`          | Handles different user responses               |
| Integer Division (`//`) | Calculates the middle number                   |
| `break`                 | Terminates the loop when the number is guessed |
| `continue`              | Skips the current iteration for invalid input  |
| `strip()`               | Removes unnecessary whitespace                 |
| `lower()`               | Converts user input into lowercase             |
| F-Strings               | Displays dynamic messages                      |

## 💻 Source Code

```
print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100.")
print("I will try to guess your number.")

low = 1
high = 100

for i in range(7):

    comp_guess = (low + high) // 2

    print(f"\nAttempt {i + 1}: Is your number {comp_guess}?")

    user_reply = input("Enter (correct/lower/higher): ").strip().lower()

    if user_reply == "correct":
        print("Congratulations! I guessed your number!")
        print(f"I guessed it in {i + 1} attempts.")
        break

    elif user_reply == "lower":
        high = comp_guess - 1

    elif user_reply == "higher":
        low = comp_guess + 1

    else:
        print("Invalid input! Please enter correct, lower, or higher.")
        continue

    if low > high:
        print("Your responses are inconsistent! Please check your answers.")
        break

else:
    print("\nI couldn't guess your number within 7 attempts.")
```

## 🔍 How Binary Search Works

Binary Search is an efficient searching algorithm that repeatedly divides the search space into two halves.

For example, suppose the user thinks of the number 73.

| Attempt | Low | High | Computer Guess | User Response |
| ------- | --: | ---: | -------------: | ------------- |
| 1       |   1 |  100 |             50 | Higher        |
| 2       |  51 |  100 |             75 | Lower         |
| 3       |  51 |   74 |             62 | Higher        |
| 4       |  63 |   74 |             68 | Higher        |
| 5       |  69 |   74 |             71 | Higher        |
| 6       |  72 |   74 |             73 | Correct       |

The computer successfully guesses 73 in just 6 attempts.

## ⚙️ How the Algorithm Works

**1. Initialize the search range**

```
low = 1
high = 100
```

The computer starts with a possible range of 1 to 100.

**2. Calculate the middle number**

```
comp_guess = (low + high) // 2
```

Integer division calculates the middle value of the current range.

**3. Update the search range**

If the user responds with `higher`:

```
low = comp_guess + 1
```

If the user responds with `lower`:

```
high = comp_guess - 1
```

**4. Repeat the process**

The computer continues narrowing down the search range until it guesses the correct number or reaches the maximum number of attempts.

## 📊 Algorithm Complexity

* **Time Complexity:** O(log₂ N)
* **Space Complexity:** O(1)

For a search range of 100 numbers, Binary Search requires a maximum of 7 guesses.

## 📚 Learning Outcome

Through this project, I learned how to implement the Binary Search Algorithm using Python.

This project improved my understanding of algorithmic thinking, search-space reduction, conditional statements, loops, and efficient problem-solving.

## 🚀 Future Improvements

* Add difficulty levels with different number ranges.
* Prevent invalid inputs from consuming attempts.
* Add a restart option.
* Allow users to select a custom number range.
* Implement the game using a `while` loop.


```
