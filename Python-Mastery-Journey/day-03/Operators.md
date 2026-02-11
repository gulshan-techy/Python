# ⚙️ Day 3: Operators & Logic Building
## Q. What is an Operator? 
## Ans. An operator is a symbol that performs a specific operation on one or more operands (variables or values). They are the foundation of logic in programming.

## 1. Arithmetic Operators (Math)
Used to perform mathematical calculations.

Addition (+) :- Adds two values. Also concatenates strings.

Subtraction (-) :- Subtracts the right operand from the left.

Multiplication (*) :- Multiplies values. Repeats strings.

Division (/) :- Divides left operand by right. Note: Always returns a float.

Floor Division (//) :- Divides and returns the integer part (removes decimal).

Modulus (%) :- Returns the remainder of the division.

Exponentiation ()** :- Raises the left operand to the power of the right.

Example:
```
x = 10
y = 3

print(x + y)    # 13 (Addition)
print(x - y)    # 7  (Subtraction)
print(x * y)    # 30 (Multiplication)

# --- Important Differences ---
print(x / y)    # 3.3333333333333335 (Float Division)
print(x // y)   # 3 (Floor Division - Integer only)
print(x % y)    # 1 (Remainder: 10 divided by 3 leaves 1)

print(x ** y)   # 1000 (10^3)
```
# --- String Magic ---
```
print("Python" + " Rocks")  # Concatenation -> "Python Rocks"
print("Hi " * 3)            # Repetition -> "Hi Hi Hi "
```
## 2. Comparison Operators (Relational)
Used to compare two values. These always return a Boolean (True or False).

Equal (==) :- Checks if values are equal.

Not Equal (!=) :- Checks if values are strictly not equal.

Greater Than (>) :- Checks if left is greater than right.

Less Than (<) :- Checks if left is less than right.

Greater/Less than or Equal (>=, <=) :- Checks boundary conditions.

Example:

```
a = 10
b = 20
c = 10

print(a == c)   # True (10 equals 10)
print(a != b)   # True (10 is not equal to 20)
print(a > b)    # False
print(a < b)    # True
```
# --- Tricky Comparisons ---
print(10 == "10")  # False (Integer 10 is NOT equal to String "10")
print("apple" == "Apple") # False (Case Sensitive)
## 3. Logical Operators (Boolean Logic)
Used to combine conditional statements (The brain of decision making).

and :- Returns True if both statements are true.

or :- Returns True if at least one statement is true.

not :- Reverses the result (True becomes False, False becomes True).

Example:

Python
x = 10
y = 5

AND Logic (Both must be True)
```
print(x > 5 and y < 10)  # True (True AND True)
print(x > 5 and y > 10)  # False (True AND False)
```
OR Logic (At least one is True)
```
print(x > 5 or y > 10)   # True (First part is True, so result is True)
```
NOT Logic (Reverse)
```
print(not(x > 5))        # False (Because x > 5 is True, NOT makes it False)
```
## 4. Assignment Operators
Used to assign values to variables efficiently.

Assign (=) :- Basic assignment.

Add & Assign (+=) :- x += 3 is short for x = x + 3.

Subtract & Assign (-=) :- x -= 3 is short for x = x - 3.

Multiply & Assign (*=) :- x *= 3 is short for x = x * 3.

Example:
```
score = 10
print(score)  # 10

score += 5    # Same as: score = score + 5
print(score)  # 15

score *= 2    # Same as: score = score * 2
print(score)  # 30

score -= 10   # Same as: score = score - 10
print(score)  # 20
```
## 5. Membership Operators
Used to test if a sequence (string, list, etc.) contains a specific value.

in :- Returns True if the value is found.

not in :- Returns True if the value is NOT found.

Example:
```
text = "Welcome to Python Mastery"

print("Python" in text)      # True
print("Java" in text)        # False
print("Java" not in text)    # True (Correct, Java is NOT there)

# Case Sensitivity Check
print("python" in text)      # False (Lower 'p' vs Upper 'P')
```
## 6. Identity Operators (Memory Check)
Used to compare objects, not if they are equal, but if they are actually the same object (same memory location).

is :- Returns True if both variables point to the same object.

is not :- Returns True if they point to different objects.

Example:
# --- Integers (Interning) ---
```
x = 10
y = 10
print(x is y)      # True (Python reuses memory for small integers)
print(x == y)      # True
```
# --- Lists (Mutable Objects) ---
```
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1      # Assignment (list3 points to list1)

print(list1 == list2) # True (Values are same)
print(list1 is list2) # False (Different memory locations!)

print(list1 is list3) # True (Same memory location)
```
## 7. Operator Precedence (BODMAS Rule)
The order in which operations are performed.

() Parentheses (Highest Priority)

**** ** Exponentiation

*, /, //, % Multiplication, Division

+, - Addition, Subtraction

Example:

```
result = 10 + 2 * 3
# Step 1: 2 * 3 = 6
# Step 2: 10 + 6 = 16
print(result) # 16

result_2 = (10 + 2) * 3
# Step 1: (10 + 2) = 12
# Step 2: 12 * 3 = 36
print(result_2) # 36
```
