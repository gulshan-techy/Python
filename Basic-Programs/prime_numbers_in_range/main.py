## Prime Numbers in a Range — Part 2

### Description
A Python program that finds all prime numbers within a user-defined range and calculates their total count.

This program extends Part 1, where a single number was checked to determine whether it was prime.

### Concepts Covered
- Nested `for` loops
- Conditional statements
- Modulus operator (`%`)
- Lists and the `append()` method
- `continue` statement
- Built-in `len()` function

### How It Works
1. Accept the starting and ending numbers.
2. Iterate through every number in the specified range.
3. Skip numbers less than or equal to 1.
4. Count the divisors of each remaining number.
5. Add numbers with exactly two divisors to a list.
6. Display the prime numbers and their total count.

### Example Output

```
Enter the starting number: 10
Enter the ending number: 30
Prime numbers: [11, 13, 17, 19, 23, 29]
Total prime numbers between 10 and 30: 6
```

### Learning Outcome
This exercise builds on the single-number prime checker and introduces nested loops, list operations, and counting results over a range.
