## Swap Two Variables

### Description

A Python program that swaps the values of two variables. It demonstrates both the traditional approach using a temporary variable and Python's multiple-assignment feature.

### Concepts Covered

* Variables and assignment
* Temporary variables
* Multiple assignment
* `print()` function

### Method 1: Using a Temporary Variable

1. Store the value of the first variable in a temporary variable.
2. Assign the second variable's value to the first variable.
3. Assign the saved value to the second variable.

### Method 2: Using Multiple Assignment

Python allows two variables to exchange values in a single statement:

```
a, b = b, a
```

### Example Output

```
After swapping:
a = 2
b = 1
```

### How to Run

```
python basic-operations/swap_two_variables.py
```

### Learning Outcome

This exercise demonstrates variable assignment, temporary storage, and Python's concise multiple-assignment syntax.
