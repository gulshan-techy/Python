 # 🐍 Day 8: For Loops in Python

## 📌 Overview
Writing the same code multiple times is boring, time-consuming, and takes up too much space. For example, if we want to print numbers from 1 to 20,000, we cannot write `print()` 20,000 times! 

That's where **Loops** come in. Today, I learned how to use `for` loops in Python to easily iterate over sequences like strings, lists, and number ranges.

---

## 🛠️ Concepts Learned

### 1. Iterating Over a String
A `for` loop can go through each character of a string one by one.

```python
name = "Abhishek"

for i in name:
    print(i)

*Output*: It will print A, b, h, i, s, h, e, k on separate lines.
```

### 2. Iterating Over a List
We can also use a for loop to go through items inside a Python list. You can even use a loop inside another loop (Nested Loop) to explore items further.

colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    print(color)
    
    # Nested loop to print every character of the color name
    for char in color:
        print(char)
### 3. The range() Function
The range() function is used to generate a sequence of numbers.
If we give one number range(n), it starts from 0 and stops at n-1.
```
# Prints numbers from 0 to 4
for k in range(5):
    print(k)

# You can also specify exactly where to start and stop:

# Prints numbers from 1 to 8 (stops at n-1)
for k in range(1, 9):
    print(k)
```

### 4. The step Parameter in range()
The range() function actually accepts three arguments: range(start, stop, step). The third argument (step) tells Python how many numbers to skip.
```
# Starts at 1, goes up to 11, jumping by 3 steps
for i in range(1, 12, 3):
    print(i)
*Output*: 1, 4, 7, 10
```

# 🐍 Day 8 (Part 2): While Loops in Python

## 📌 Overview
In the previous video, we learned about `for` loops, which are great when we know exactly how many times a loop should run. However, sometimes we want a loop to keep running *as long as a specific condition is true*. 

That's where **`while` loops** come in! Today, I learned how `while` loops work in Python, how to avoid infinite loops, and how to use the `else` block with them.

---

## 🛠️ Concepts Learned

### 1. Basic `while` Loop Structure
A `while` loop checks a condition first. If the condition is `True`, it runs the code block. It keeps doing this until the condition becomes `False`.

```
# Printing numbers from 0 to 2
i = 0

while i < 3:
    print(i)
    i = i + 1  # Incrementing the value so the loop eventually stops

print("Done with the loop!")

0
1
2
Done with the loop!
```

### 2. User Input inside a while Loop
while loops are very useful when you want to keep asking a user for input until they type a specific value.
```
# Keep asking for a number until the user enters a number greater than 38
i = int(input("Enter a number: "))

while i <= 38:
    i = int(input("Enter a number: "))
    print("You entered:", i)

print("You finally entered a number greater than 38!")
```

### 3. Decrementing while Loop
You can also run loops backwards (countdown) by subtracting the value instead of adding to it.
```
count = 5

while count > 0:
    print(count)
    count = count - 1  # Decrementing

print("Liftoff! 🚀")
```

### 4. 🚨 The Infinite Loop Danger
If you forget to update your counter variable (e.g., you forget to write i = i + 1), the condition will always stay True. This creates an infinite loop, which will freeze your terminal and force you to forcefully kill the program.
```
# ❌ DANGEROUS CODE (Will print '5' forever)
count = 5

while count > 0:
    print(count)
    # The program will get stuck here because count is never reduced!
```

### 5. while Loop with else
In Python, you can use an else block directly after a while loop. The code inside the else block will only execute when the while condition naturally becomes False.

```
count = 3

while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside the else block because the condition is now False!")
```
