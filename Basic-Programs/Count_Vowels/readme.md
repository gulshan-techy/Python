# 🐍 Count Vowels in a String Using Python

## 📌 About the Project

This beginner-friendly Python program counts the occurrences of each vowel (`a`, `e`, `i`, `o`, and `u`) in a paragraph entered by the user.

It handles both uppercase and lowercase vowels by converting the text to lowercase before checking each character.

## 🎯 Concepts Covered

- `input()` — Accepting text from the user.
- Strings — Working with text data.
- `lower()` — Converting text to lowercase.
- `for` loop — Iterating through each character.
- `if-elif` statements — Checking individual vowels.
- Counters — Tracking the number of occurrences.
- `print()` — Displaying individual vowel counts and the total.

## 💻 Python Code

```
para = input("Enter a paragraph: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for char in para.lower():
    if char == "a":
        a += 1
    elif char == "e":
        e += 1
    elif char == "i":
        i += 1
    elif char == "o":
        o += 1
    elif char == "u":
        u += 1

print("Total a:", a)
print("Total e:", e)
print("Total i:", i_count)
print("Total o:", o)
print("Total u:", u)
print("Total vowels:", a + e + i + o + u)
```

## ▶️ Sample Output

```
Enter a paragraph: Hello Gulshan
Total a: 1
Total e: 1
Total i: 0
Total o: 2
Total u: 1
Total vowels: 5
```

## ⚙️ How to Run

Make sure Python 3 is installed on your system.

Run the following command from the directory containing the file:

```
python count_vowels.py
```

Depending on your system, use `python3` instead of `python` if required.

## 📚 What I Learned

- How to iterate through a string character by character.
- How to count occurrences using counter variables.
- How to handle uppercase and lowercase characters.
- How to use `if-elif` statements for character matching.
- How to calculate the total number of vowels.

## 🚀 Learning Journey

This program is part of my Python fundamentals practice. I am strengthening my programming logic and string manipulation skills as I work toward my goals in Cloud Computing, DevOps, and Automation.

**Learning Python one program at a time!** 🐍
