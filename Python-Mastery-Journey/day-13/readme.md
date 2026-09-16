# 🐍 Day 13: The `finally` Keyword in Python

## 📌 Overview
In the previous lesson, we learned how to handle errors using `try` and `except` to prevent our programs from crashing. Today, we are adding one more piece to the puzzle: the **`finally`** block.

The `finally` block contains code that is **always executed**, no matter what happens in the `try` or `except` blocks.

---

## 🛠️ Concepts Learned

### 1. What does `finally` do?
When you use a `try-except-finally` block, the code inside `finally` is guaranteed to run. 
* If the `try` block succeeds, `finally` runs.
* If the `try` block fails and throws an error (handled by `except`), `finally` still runs.

```
try:
    num = int(input("Enter an integer: "))
    print(num)
except ValueError:
    print("That is not a valid integer!")
finally:
    print("I am always executed!")
```

### 2. The Big Interview Question: Why use finally?
You might be wondering: "Why do I need a finally block? If I want code to always run, why don't I just write it normally outside the try-except block?"

Look at this example:
```
try:
    num = int(input("Enter a number: "))
except:
    print("Error occurred.")

# Normal print statement outside the block
print("I am always executed!")
```
If you just write code outside the block like above, it seems to do the exact same thing as finally. But there is one major exception: Functions with return statements.

### 3. The True Power of finally (Inside Functions)
When a function hits a return statement, it immediately stops and exits. No code below the return statement will execute.

However, finally ignores this rule. If a try or except block tries to return out of the function, Python will pause the return, execute the finally block, and then return the value.

```
def my_function():
    try:
        my_list = [1, 5, 6, 7]
        i = int(input("Enter an index: "))
        print(my_list[i])
        return 1  # Function tries to exit here if successful
        
    except:
        print("Some error occurred")
        return 0  # Function tries to exit here if an error happens

    finally:
        # This will STILL RUN, even though the function already returned!
        print("I will execute no matter what!")

    print("I will NOT execute because the function returned.")

# Calling the function
x = my_function()
print("Returned value:", x)
```

### 4. When to use ***finally***
The finally block is generally used for clean-up tasks. For example:

Closing a file that you opened inside the try block.

Closing a database connection.

Freeing up memory.

If you don't use finally, and your function hits a return statement (or crashes with an unhandled error), your file or database connection might remain open and cause memory leaks!
