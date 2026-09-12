# 🐍 Day 9: Break and Continue Statements in Python

## 📌 Overview
Sometimes, we don't want a loop to run its full course. We might want to stop the loop entirely if a certain condition is met, or we might want to skip just one specific step and move on to the next.

Today, I learned how to control the flow of loops using `break` and `continue` statements in Python.

---

## 🛠️ Concepts Learned

### 1. The `break` Statement
The `break` statement is used to exit or "break out" of a loop completely. When Python sees a `break` statement, it immediately stops the loop, ignores the rest of the iterations, and moves to the code below the loop.

```
# Printing a multiplication table of 5, but stopping at 5 * 10
for i in range(1, 15):
    if i == 11:
        print("Loop is broken! Exiting...")
        break  # The loop stops here
    
    print("5 X", i, "=", 5 * i)

print("I am outside the loop now.")
```

### 2. The continue Statement
The continue statement is used to skip the current iteration of the loop. When Python sees continue, it skips all the code below it for that specific step and jumps directly to the next iteration of the loop.

```
# Printing a multiplication table of 5, but skipping 5 * 10
for i in range(1, 13):
    if i == 10:
        print("Skipping the 10th iteration...")
        continue  # Skips only this step and moves to i = 11
    
    print("5 X", i, "=", 5 * i)
```

### ***Quick Comparison***
- break: "Leave the loop completely and don't come back."
- continue: "Skip this specific turn, but keep going with the next ones."
