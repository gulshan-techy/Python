## Part 5: Inverted Right Triangle Star Pattern

### Description
A Python program that prints an inverted right triangle using stars (`*`). Each new row contains one fewer star than the previous row.

### Code
```
num = 5

for i in range(num, 0, -1):
    print("*" * i)
```

### Output
```text
*****
****
***
**
*
```

### Concepts Covered
- `for` loops
- Reverse iteration using `range()`
- String repetition using the `*` operator
- Controlling the number of characters printed

### How It Works
1. Set the number of rows to 5.
2. Iterate from 5 down to 1.
3. Print the star character repeated `i` times in each row.
4. The number of stars decreases by one in every iteration.

### Learning Outcome
This exercise demonstrates reverse iteration and string repetition to create a decreasing star pattern.
