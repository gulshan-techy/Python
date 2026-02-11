# 1. Arithmetic Operators
print("\n--- 1. Arithmetic Operations ---")
x, y = 10, 3
print(f"Addition (10 + 3): {x + y}")
print(f"Subtraction (10 - 3): {x - y}")
print(f"Multiplication (10 * 3): {x * y}")
print(f"Float Division (10 / 3): {x / y}")
print(f"Floor Division (10 // 3): {x // y}")
print(f"Modulus (Remainder): {x % y}")
print(f"Power (10^3): {x ** y}")

# String Arithmetic
print("Python" + " Rocks")   # Concatenation
print("Hi " * 3)             # Repetition

# 2. Comparison Operators
print("\n--- 2. Comparison Operations ---")
a, b = 10, 20
print(f"Is {a} == {b}? {a == b}")
print(f"Is {a} != {b}? {a != b}")
print(f"Is {a} < {b}? {a < b}")

# 3. Logical Operators
print("\n--- 3. Logical Operations ---")
x, y = 10, 5
print(f"Check (x > 5 and y < 10): {x > 5 and y < 10}") # True AND True
print(f"Check (x > 5 or y > 10): {x > 5 or y > 10}")   # True OR False
print(f"Check (not x > 5): {not(x > 5)}")              # NOT True

# 4. Assignment Operators
print("\n--- 4. Assignment Operations ---")
score = 10
score += 5   # score = 10 + 5
print(f"Score after += 5: {score}")

score *= 2   # score = 15 * 2
print(f"Score after *= 2: {score}")

score -= 10  # score = 30 - 10
print(f"Score after -= 10: {score}")

# 5. Membership Operators
print("\n--- 5. Membership Operations ---")
text = "Welcome to Python Mastery"
print(f"Is 'Python' in text? {'Python' in text}")
print(f"Is 'Java' not in text? {'Java' not in text}")
print(f"Case Sensitivity Check ('python'): {'python' in text}")

# 6. Identity Operators (Most Important)
print("\n--- 6. Identity Operations (is vs ==) ---")
# Integers (Immutable & Interned)
x, y = 10, 10
print(f"Integers x is y? {x is y}") # True
# Lists (Mutable)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 
print(f"List Equality (==): {list1 == list2}") # True (Values are same)
print(f"List Identity (is): {list1 is list2}") # False (Memory is diffrent)
print(f"List Reference (is): {list1 is list3}") # True (Same object)
