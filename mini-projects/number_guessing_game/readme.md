# 🎯 Number Guessing Game

## 📌 Overview

The Number Guessing Game is a beginner-friendly Python project in which the computer randomly generates a number between 0 and 100. The user gets a maximum of 15 attempts to guess the correct number.

After each guess, the program provides hints indicating whether the actual number is higher or lower than the user's guess.

The game also handles invalid inputs, validates the allowed number range, tracks remaining attempts, and displays the correct number when the user runs out of attempts.

## ✨ Features

- Generates a random number between 0 and 100.
- Provides a maximum of 15 attempts.
- Handles invalid inputs using exception handling.
- Validates user input to ensure it is within the 0–100 range.
- Displays the remaining attempts.
- Provides higher or lower hints after incorrect guesses.
- Stops the game when the correct number is guessed.
- Displays a Game Over message when all attempts are exhausted.
- Reveals the correct number at the end of the game.

## 🛠️ Python Concepts Used

| Concept | Purpose |
|---|---|
| Random Module | Generates a random number |
| Variables | Stores game data |
| `input()` | Accepts user input |
| `int()` | Converts input into an integer |
| `try-except` | Handles invalid input |
| `for` Loop | Controls the maximum attempts |
| `if-elif-else` | Compares the guessed number |
| `continue` | Skips the current iteration |
| `break` | Terminates the loop after a correct guess |
| `for-else` | Displays the Game Over message |
| F-Strings | Displays dynamic messages |

## 💻 Source Code

```
import random

computer_num = random.randint(0, 100)
max_attempts = 15

print("Welcome to Number Guessing Game!")
print(f"You have maximum {max_attempts} attempts to guess the number between 0 and 100.")

for i in range(max_attempts):

    print(f"\nAttempts remaining: {max_attempts - i}")

    try:
        user_num = int(input("Guess The Number: "))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    if user_num < 0 or user_num > 100:
        print("Please enter a number between 0 and 100.")
        continue

    if user_num == computer_num:
        print(f"Congratulations! You guessed the correct number: {computer_num}")
        break

    elif computer_num > user_num:
        print("Number is Higher, Try Again!")

    else:
        print("Number is Lower, Try Again!")

else:
    print("\nGame Over! You have used all your attempts.")
    print(f"The correct number was: {computer_num}")
```

## 📸 Example Output

```
Welcome to Number Guessing Game!
You have maximum 15 attempts to guess the number between 0 and 100.

Attempts remaining: 15
Guess The Number: 30
Number is Higher, Try Again!

Attempts remaining: 14
Guess The Number: 70
Number is Lower, Try Again!

Attempts remaining: 13
Guess The Number: 50
Congratulations! You guessed the correct number: 50
```

*Note: The example assumes the randomly generated number is 50.*

## 📚 Learning Outcome

Through this project, I practiced Python loops, conditional statements, exception handling, input validation, random number generation, and loop control statements.

## 🚀 Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Allow users to restart the game.
- Add a scoring system.
- Track the total number of guesses.
- Prevent invalid inputs from consuming an attempt.
```
