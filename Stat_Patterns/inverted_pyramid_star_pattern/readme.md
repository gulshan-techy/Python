## Part 4: Inverted Pyramid Star Pattern

### Description
A Python program that prints an inverted pyramid using stars (`*`). The pattern starts with the widest row and decreases by two stars in each subsequent row.

### Code
```
num = 5

for i in range(num, 0, -1):
    spaces = num - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
```

### Output
```
*********
 *******
  *****
   ***
    *
```

### Concepts Covered
- `for` loops and `range()`
- Reverse iteration using a negative step
- Arithmetic expressions
- String repetition using `*`
- String concatenation and spacing

### How It Works
1. Initialize the number of rows.
2. Iterate from the number of rows down to 1.
3. Increase leading spaces for each row.
4. Decrease the number of stars by two per row.
5. Print the spaces followed by the stars.



### Learning Outcome
This exercise demonstrates reverse iteration and how to control spacing and star counts to generate an inverted pyramid.
