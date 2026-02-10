# 🧬 Day 2: Data Types, Definitions & String Operations

## 1. What is a Data Type?
In Computer Science, a **Data Type** classifies a value. It tells the compiler or interpreter:
1.  **Storage:** How the data is stored in memory.
2.  **Operations:** What you can do with it (e.g., you can multiply numbers, but you can't multiply text).

---

## 2. Numeric Types (Numbers)
Python handles numbers using three distinct types:

### 🔹 A. Integer (`int`)
* **Definition:** Represents whole numbers (positive, negative, or zero) **without** decimals.
* **Feature:** In Python 3, integers have **unlimited precision** (they can be as big as your memory allows).
* **Example:**
    ```python
    x = 100
    y = -50
    ```

### 🔹 B. Floating Point (`float`)
* **Definition:** Represents real numbers **with** a decimal point.
* **Feature:** Stored in binary format (IEEE 754 standard). They are approximations.
* **Example:**
    ```python
    pi = 3.14159
    temp = -10.5
    ```

### 🔹 C. Complex Number (`complex`)
* **Definition:** Numbers with a **Real** part and an **Imaginary** part. Used in advanced mathematics/engineering.
* **Example:**
    ```python
    z = 2 + 3j  # (2 is real, 3j is imaginary)
    ```

---

## 3. Boolean Type (`bool`)
* **Definition:** Represents a logical truth value. It can only be `True` or `False`.
* **Internal Working:** In Python, `True` is treated as `1` and `False` is treated as `0`.
* **Example:**
    ```python
    is_active = True
    has_error = False
    ```

---

## 4. Text Type: String (`str`)
* **Definition:** A String is a **sequence of characters** enclosed in quotes (single `'` or double `"`).
* **Key Property:** Strings are **Immutable**. This means once you create a string, you cannot change a character inside it. You must create a new string.

### 🔹 String Indexing (Visualizing Memory)
Strings are stored as an ordered list of characters. We can access them using an **Index** (Position).



* **Positive Index:** Starts from `0` (Left to Right).
* **Negative Index:** Starts from `-1` (Right to Left).

text = "PYTHON"
# P  Y  T  H  O  N
# 0  1  2  3  4  5  (Positive Index)
#-6 -5 -4 -3 -2 -1  (Negative Index)

print(text[0])   # Output: 'P'
print(text[-1])  # Output: 'N'

#Indexing :- Indexing means accessing individual characters of a string using their position (index). In Python, indexing starts from 0 for the first character .Negative indexing allows access from the end of the string.

s = "This is Python"
print(s[0])    # 'T' → first character
print(s[5])    # 'i' → sixth character
print(s[-1])   # 'n' → last character
print(s[-6])   # 'P' → sixth from the end

#Slicing :- Slicing means extracting a substring from the original string. 
Syntax: string[start:end:step]
start→ index where slice begins (inclusive)
end → index where slice ends (exclusive)
step → interval (default is 1)

s = "This is Python"
print(s[0:4])     # "This" → characters from index 0 to 3
print(s[5:7])     # "is"   → characters from index 5 to 6
print(s[:4])      # "This" → from start to index 3
print(s[8:])      # "Python" → from index 8 to end
print(s[::2])     # "Ti sPto" → every 2nd character
print(s[::-1])    # "nohtyP si sihT" → reversed string

# Basic String Operation
s = "This is Python"
print(len(s))          # Length of string → 13
print(s.upper())       # Convert to uppercase → "THIS IS PYTHON"
print(s.lower())       # Convert to lowercase → "this is python"
print(s.title())       # Title case → "This Is Python"
print(s.replace("Python", "Awesome"))  # Replace word → "This is Awesome"
print("Python" in s)   # Check substring → True
print(s.find("is"))    # Find position → 2
print(s.index("Python")) # Index of substring → 8
words = s.split()      # Split into list → ['This', 'is', 'Python']
print(words)
joined = "-".join(words)  # Join with separator → "This-is-Python"
print(joined)
