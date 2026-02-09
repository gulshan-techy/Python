# 📘 Day 1: Python Architecture & Variable Internals

## 1. The 5 W's of Python (History & Context)
Before writing code, it's crucial to understand the tool.

| Question | Answer |
| :--- | :--- |
| **Who** | Created by **Guido van Rossum**. |
| **When** | Conceived in **late 1980s**, first released in **1991**. |
| **Where** | At **CWI** (Centrum Wiskunde & Informatica) in the Netherlands. |
| **Why** | To create a language that was capable of Exception Handling (like Modula-3) but easy to use like Shell scripts. It was a successor to the **ABC** language. |
| **What** | An interpreted, high-level, general-purpose programming language. |

> **DevOps Note:** Python is often called the "glue" language because it easily connects various components (Cloud APIs, OS commands, Databases), making it perfect for automation.

---

## 2. Variables: The Engineering Deep Dive

### 🔹 What is a Variable in Python?
In languages like C or Java, a variable is a **container** (a box in memory) that holds a value.
In Python, a variable is a **Reference** (a name tag) that points to an object in memory.

When you write a = 10:
Python creates an object 10 in memory.
It puts a tag named a on it. If you write b = 10, Python doesn't create a new object. It just puts another tag b on the same object to save memory! 🤯

a = 10
b = 10

print(id(a))  # memory address of object 10
print(id(b))  # same as id(a)


### 🔹 How to Define?
Python is **Dynamically Typed**, meaning you don't need to declare the type (e.g., `int x`). The Python Interpreter infers it at runtime.

```python
user_name = "Gulshan"  # String
server_count = 5       # Integer
is_active = True       # Boolean
cpu_load = 45.5        # Float
