# 🚀 Python While Loops - Day #9

## 📖 Introduction
Python has two main types of loops: `for` and `while`. 
We use a `while` loop when we want to execute a block of code continuously **as long as a given condition is True**. As soon as the condition becomes False, the interpreter comes out of the loop.

---

## 💻 1. Basic While Loop (Incrementing)
Here, the loop will run as long as `i` is less than or equal to 3. Once `i` becomes 4, the loop stops.

```python
i = 0
while i <= 3:
    print(i)
    i = i + 1  # Incrementing the value of i

print("Done with the loop")
```

## ⌨️ 2. While Loop with User Input
While loops are highly useful for complex conditions, like taking input from a user continuously until they enter a specific number.

```python
i = int(input("Enter a number: "))

while i <= 38:
    i = int(input("Enter a number: "))
    print(i)

print("Done with the loop")
```

## 📉 3. Decrementing While Loop (Reverse Loop)
In this loop, the value decreases after every iteration (ulta loop).

```python
count = 5
while count > 0:
    print(count)
    count = count - 1  # Decrementing the value
```

## ♾️ 4. Infinite Loop (⚠️ Warning)
If you forget to update the variable correctly, the condition will always remain True, and the loop will run forever! 

```python
# Example of an infinite loop
count = 5
while count > 0:
    print(count)
    count = count + 1  # Mistake: increasing instead of decreasing
```
*Tip: If you get stuck in an infinite loop, press `Ctrl + C` in your terminal to manually stop it.*

## 🔀 5. While Loop with `else` Block
Python allows you to use an `else` statement with a `while` loop. The `else` block executes exactly once **when the while condition becomes False** and the loop finishes naturally.

```python
count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")
```
