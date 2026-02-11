# 📦 Day 4: Data Collections - Lists & Tuples
## Q. What are Collections?
## Ans. Up until now, we used variables to store single values (e.g., x = 10). But to store multiple items (like 100 IP addresses or 50 filenames) in a single variable, Python provides built-in data structures called Collections.

## 1. Python Lists (The Flexible Container)
#### A List is an ordered collection of items. It is Mutable, meaning you can modify it (add, delete, or change items) after creation.

Syntax :- Square brackets []

#### Characteristics of List :

Ordered :- Items maintain their order.

Mutable :- You can change values after creation.

Heterogeneous :- Can store mixed data types (Integers, Strings, even other Lists).

Dynamic :- Expands automatically as you add items.

Common List Methods:

append(item) :- Adds an item to the end of the list.

insert(index, item) :- Adds an item at a specific index position.

remove(item) :- Removes the first occurrence of the specified value.

pop(index) :- Removes and returns the item at the specific index (default is the last item).

sort() :- Sorts the list in ascending order.

reverse() :- Reverses the order of the list.

Example:

### Creating a List
servers = ["web-01", "db-01", "cache-01"]

print(servers)

### Adding items
servers.append("web-02")       # ['web-01', 'db-01', 'cache-01', 'web-02']
servers.insert(1, "aws-lb")    # Inserts at index 1

### Modifying items
servers[2] = "database-PROD"   # Changing 'db-01' to 'database-PROD'

### Removing items
servers.remove("cache-01")     # Removes by value
last_server = servers.pop()    # Removes last item ('web-02')

print(servers)

## 2. Python Tuples (The Fixed Container)
#### A Tuple is also an ordered collection, but it is Immutable. Once created, it cannot be changed. Think of it as a "Read-Only" List.

Syntax :- Parentheses ()

#### Characteristics of Tuple:

Ordered :- Items maintain their order.

Immutable :- No addition, deletion, or modification allowed.

Faster :- Since they are fixed, Python optimizes them in memory.

Tuple Methods: Since tuples are immutable, they only have two main methods:

count(item) :- Returns the number of times a value appears in the tuple.

index(item) :- Returns the index of the first occurrence of the value.

Example:

### Creating a Tuple
aws_regions = ("us-east-1", "us-west-2", "ap-south-1")

print(aws_regions[0])  # Accessing is allowed

###  --- Immutability Check ---
###  aws_regions[0] = "eu-central-1"  
###  ❌ TypeError: 'tuple' object does not support item assignment

## 3. List vs Tuple: The Engineering Breakdown
### Mutability

List :- Mutable (Items can be changed).

Tuple :- Immutable (Items are fixed).

### Performance

List :- Slower (Due to dynamic memory allocation logic).

Tuple :- Faster (Fixed memory allocation).

### Memory Usage

List :- Consumes more memory (Has overhead for future growth).

Tuple :- Consumes less memory.

### Methods

List :- Many (append, pop, sort, clear, etc.).

Tuple :- Few (only count, index).

## 4. Real-World Use Cases (DevOps & Cloud)
### When to use a List?

Storing a list of EC2 Instance IDs (which might scale up or down).

Collecting logs from a server (new logs are constantly appended).

A queue of jobs/tasks to be processed.

### When to use a Tuple?

Storing Database Credentials (Host, Port, DB_Name) - strictly shouldn't change.

Defining fixed Configuration constants (e.g., ALLOWED_EXTENSIONS = ('.jpg', '.png')).

Return values from a function (Returning multiple values safely).

## 5. Memory Comparison Proof (Engineering Insight)
Let's prove that Tuples are more efficient using the sys module.

Example:

import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("List Size:", sys.getsizeof(my_list), "bytes")
print("Tuple Size:", sys.getsizeof(my_tuple), "bytes")

# Conclusion: Tuple will always take less memory than List for the same data.
