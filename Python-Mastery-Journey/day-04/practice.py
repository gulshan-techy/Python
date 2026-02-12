# A. Creating & Accessing Lists

# 1. Creating Lists
tools = ["Docker", "Kubernetes", "Jenkins", "Terraform", "Ansible"]

# 2. Accessing Items (Indexing)
print(tools[0])      # Output: Docker (First Item)
print(tools[-1])     # Output: Ansible (Last Item)

# 3. Slicing (The Surgeon's Knife)
print(tools[0:2])    # Output: ['Docker', 'Kubernetes'] (Index 0 to 1)
print(tools[2:])     # Output: ['Jenkins', 'Terraform', 'Ansible'] (Index 2 to end)
print(tools[::-1])   # Output: ['Ansible', ..., 'Docker'] (Reverse List)

# B. Adding Elements (Append vs Insert vs Extend)

aws_services = ["EC2", "S3"]

# 1. Append (Add to end)
aws_services.append("Lambda")
# Result: ['EC2', 'S3', 'Lambda']

# 2. Insert (Add at specific index)
aws_services.insert(1, "RDS")
# Result: ['EC2', 'RDS', 'S3', 'Lambda']

# 3. Extend (Merge lists)
more_services = ["IAM", "VPC"]
aws_services.extend(more_services)
# Result: ['EC2', 'RDS', 'S3', 'Lambda', 'IAM', 'VPC']

# C. Removing Elements

users = ["Alice", "Bob", "Charlie", "Dave"]

# 1. Remove by Value
users.remove("Bob")       
# Result: ['Alice', 'Charlie', 'Dave']

# 2. Remove by Index (pop)
kicked_user = users.pop() # Removes last item ('Dave')
print(kicked_user)        # Output: Dave

# 3. Clear everything
users.clear()             
# Result: []

# D. List Comprehension (The "Pro" Way)

nums = [1, 2, 3, 4, 5]

# Traditional Way
squares = []
for n in nums:
    squares.append(n ** 2)

# Pythonic Way (List Comprehension)
squares = [n ** 2 for n in nums] 
# Output: [1, 4, 9, 16, 25]

#===============================================================================================================================

# A. Creating Tuples

# Simple tuple
numbers = (1, 2, 3, 4)
print(numbers)   # Output: (1, 2, 3, 4)

# Mixed data types
mixed = ("apple", 10, 3.14, True)
print(mixed)     # Output: ('apple', 10, 3.14, True)

# Empty tuple
empty = ()
print(empty)     # Output: ()

# Tuple using constructor
names = tuple(["Alice", "Bob", "Charlie"])
print(names)     # Output: ('Alice', 'Bob', 'Charlie')

# B. Accessing Tupel Elements

fruits = ("apple", "banana", "cherry")

print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry

# C. Nested Tuples

nested = (1, (2, 3), (4, 5, 6))
print(nested[1])       # Output: (2, 3)
print(nested[2][1])    # Output: 5

# D.  Tuple Operations

tup = (10, 20, 30, 40)

# Length
print(len(tup))   # Output: 4

# Concatenation
new_tup = tup + (50, 60)
print(new_tup)    # Output: (10, 20, 30, 40, 50, 60)

# Repetition
repeat = ("Hi",) * 3
print(repeat)     # Output: ('Hi', 'Hi', 'Hi')

# E. Tuple Packing & Unpacking

# Packing
person = ("John", 25, "Engineer")

# Unpacking
name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Engineer

# F. Immutability Example

tup = (1, 2, 3)
# tup[0] = 10   # ❌ Error: 'tuple' object does not support item assignment

# G. Tuple Methods

tup = (1, 2, 2, 3, 4)

print(tup.count(2))   # Output: 2
print(tup.index(3))   # Output: 3




# 3. THE ENGINEERING INSIGHT (Memory & Speed)

print("\n--- C. PERFORMANCE ENGINEERING ---")

# A. Memory Check (Size Comparison)
# We are creating large datasets to see the difference clearly
list_data = [0, 1, 2, "Python", True] * 1000 
tuple_data = (0, 1, 2, "Python", True) * 1000

print(f"List Memory:  {sys.getsizeof(list_data)} bytes")
print(f"Tuple Memory: {sys.getsizeof(tuple_data)} bytes")

# B. Speed Check (Creation Time)
# Checking how much time it takes to create 1 Million Lists vs Tuples
# We use timeit because it runs the code multiple times to get an average result
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"\nList Creation Time (1M times):  {list_time:.4f} sec")
print(f"Tuple Creation Time (1M times): {tuple_time:.4f} sec")

# C. Conclusion
# Calculate percentage difference
diff = ((list_time - tuple_time) / list_time) * 100
print(f"\n✅ Conclusion: Tuples are {diff:.2f}% FASTER and take LESS memory!")

