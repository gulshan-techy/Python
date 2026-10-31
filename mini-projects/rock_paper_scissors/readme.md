# Python Mini Games

## Rock Paper Scissors Game

### Description

A simple command-line Rock Paper Scissors game built using Python. The user plays against the computer, which randomly selects one of the three choices.

### Game Rules

* Rock beats Scissors.
* Scissors beats Paper.
* Paper beats Rock.
* If both players choose the same option, the game is a draw.

### Concepts Covered

* Importing Python modules
* `random.choice()` function
* Lists
* User input using `input()`
* String methods: `strip()` and `lower()`
* Conditional statements (`if-elif-else`)
* Input validation

### How It Works

1. Accept the user's choice: rock, paper, or scissors.
2. Normalize the input using `strip()` and `lower()`.
3. Validate the user's choice.
4. Use `random.choice()` to generate the computer's choice.
5. Compare both choices using conditional statements.
6. Display the winner or declare a draw.

### Example Output

```
Enter your choice (rock, paper, scissors): rock
You chose: rock
Computer chose: scissors
You Won!
```

### Learning Outcome

This project demonstrates how to use Python's random module, user input, lists, string methods, and conditional logic to build a simple interactive game.

### Future Improvements

* Add a best-of-3 game mode.
* Add score tracking for the user and computer.
* Allow users to play multiple rounds.
* Add an option to exit the game.
