print(" 🚀 Day 20 Practice: 'is' vs '==' in Python")

# 1 Lists Comparison (Mutable Objects - Different memory locations)
print("\n 1. LISTS COMPARISON (Mutable Objects):")
a = [1, 2, 3]
b = [1, 2, 3]
print(f" a = {a}")
print(f" b = {b}")
print(f" a == b (Do values match?): {a == b}")
print(f" a is b (Are they the exact same object in RAM?): {a is b}")

# 2 Integers Comparison (Python Memory Optimization / Caching)
print("\n 2. INTEGER COMPARISON (Python Optimization):")
x = 3
y = 3
print(f" x = {x}, y = {y}")
print(f" x == y (Do values match?): {x == y}")
print(f" x is y (Same memory location due to optimization?): {x is y}")

#  3. Checking for None (Best Practice)
print("\n 3. CHECKING FOR 'None' (Best Practice):")
user_status = None
print(f" user_status = {user_status}")
print(f" user_status is None: {user_status is None}\n")

print(" 'is' vs '==' Concepts Executed Successfully! ")
