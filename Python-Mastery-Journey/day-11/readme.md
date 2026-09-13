# 🐍 Day 11: Functions in Python (Part 2) - Arguments & Return

## 📌 Overview
In the previous lesson, we learned how to create basic functions and pass arguments to them. Today, we dive deeper into **Function Arguments** and the **`return` statement**. 

We learned that there are different ways to pass arguments to a function, and how to get a computed value back from a function using `return`.

---

## 🛠️ Concepts Learned

### 1. Default Arguments
You can assign a default value to an argument when defining the function. If you call the function without providing a value for that argument, it will automatically use the default value.

```
# Here, 'b' has a default value of 1
def calculate_average(a, b=1):
    average = (a + b) / 2
    print("The average is:", average)

calculate_average(9)       # Output: 5.0 (Uses a=9, b=1)
calculate_average(9, 5)    # Output: 7.0 (Uses a=9, b=5, ignoring the default)
```

### 2. Keyword Arguments
When calling a function, you can pass arguments using their parameter names. This is called Keyword Arguments. When you do this, the order does not matter.

```
def print_name(first_name, last_name):
    print("Hello", first_name, last_name)

# Passing arguments by name in a different order
print_name(last_name="Watson", first_name="Emma") 
# Output: Hello Emma Watson
```

### 3. Required Arguments
If an argument does not have a default value, it is a Required Argument. You must provide a value for it when calling the function, otherwise, Python will throw an error.

```
# Both 'a' and 'b' are required here
def add_numbers(a, b):
    print(a + b)

add_numbers(10)  # ❌ TypeError: missing 1 required positional argument: 'b'
```

### 4. Variable-Length Arguments (*args)
What if you want to calculate the average of 5 numbers? Or 10 numbers? You don't need to create a function with 10 variables! You can use a single asterisk * before the parameter name. This packs all the provided values into a Tuple.


# The *numbers argument can take any number of inputs
def calculate_average(*numbers):
    sum_total = 0
 ```   
    for i in numbers:
        sum_total = sum_total + i
        
    average = sum_total / len(numbers)
    print("Average is:", average)

calculate_average(5, 6, 7, 1)  # You can pass 4 numbers
calculate_average(10, 20)      # Or just 2 numbers
```

### 5. The return Statement
Until now, our functions were just printing the results to the screen. But what if we want to store that result in a variable to use it later in our program? We use the return statement.

When Python sees return, it says: "Stop the function and go back with this value!"

```
def get_average(*numbers):
    sum_total = 0
    for i in numbers:
        sum_total += i
    
    return sum_total / len(numbers)  # Returns the value instead of printing it

# Storing the returned value in variable 'c'
c = get_average(5, 6, 7, 1)

print("The computed value is:", c)
```
Note: If a function does not have a return statement, it automatically returns None. Also, any code written after the return statement inside a function will not be executed.
