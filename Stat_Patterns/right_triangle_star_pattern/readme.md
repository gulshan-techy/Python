## Part 2: Right Triangle Star Pattern

### Description
A Python program that prints a right triangle star pattern using nested `for` loops. Each row contains one more star than the previous row.

### Code
```
num = 6

for i in range(1, num + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

### Output
```text
*
* *
* * *
* * * *
* * * * *
* * * * * *
```

### Concepts Covered
- Nested `for` loops
- The `range()` function
- Iteration and row-by-row pattern generation
- The `print()` function
- The `end` parameter

### How It Works
1. Initialize `num` with the number of rows.
2. The outer loop controls the rows, running from 1 to `num`.
3. The inner loop prints as many stars as the current row number.
4. An empty `print()` moves the output to the next line after each row.

### Learning Outcome
This exercise demonstrates how nested loops can generate a triangle pattern by increasing the number of stars in each row.
