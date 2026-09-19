# 🐍 Day 16: File Handling in Python (Part 1)

## 📌 Overview
So far, all the data we generated in our programs was lost the moment the program finished running. If we want to save data permanently (like saving a game's high score or storing student marks), we need to write that data to a file. 

Today, I learned the basics of **File Handling (File IO)** in Python. 

---

## 🛠️ Concepts Learned

### 1. Opening a File
To interact with a file in Python, the very first step is to open it using the built-in `open()` function. 

The `open()` function takes two main arguments:
1.  **File Name:** The name of the file you want to open (e.g., `"myfile.txt"`).
2.  **Mode:** What you want to do with the file (Read, Write, or Append).

### 2. The 3 Main File Modes
*   **`'r'` (Read):** Opens a file for reading. If the file does not exist, it throws an error. (This is the default mode).
*   **`'w'` (Write):** Opens a file for writing. **Warning:** This will overwrite any existing content in the file. If the file doesn't exist, it creates a new one.
*   **`'a'` (Append):** Opens a file to add content at the very end. It does NOT overwrite existing text. If the file doesn't exist, it creates a new one.

### 3. Reading from a File
To read the contents of a file, we open it in `'r'` mode and use the `read()` method.

```
# Open the file in 'read' mode (or 'rt' for read text)
f = open('myfile.txt', 'r')

# Extract all text from the file
text = f.read()
print(text)

# Always close the file when you are done!
f.close()
```

### 4. Writing to a File
To write data, we use 'w' mode. If we use 'w', the old data is erased.
Note: If you don't call f.close(), the text might not actually get saved to the file!


# Open the file in 'write' mode
```
f = open('myfile.txt', 'w')

# Write text to the file
f.write("Hello, World!")

# Save and close the file
f.close()
```
### 5. Appending to a File
If we want to keep our old data and just add a new line at the end, we use 'a' mode.

```
# Open the file in 'append' mode
f = open('myfile.txt', 'a')

# Add text to the end of the file
f.write("This line is added at the end.")

f.close()
```
6. The "Smart" Way: Using with
Always remembering to type f.close() can be annoying. If you forget it, it's like opening the fridge door to take out an ice cream and leaving the door wide open!

Python gives us a smarter way using the with statement. When you use with, Python automatically closes the file for you as soon as the block of code finishes.

```
# Using the 'with' statement (No f.close() needed!)
with open('myfile.txt', 'a') as f:
    f.write("I am inside the 'with' block. I will close automatically!")
    
# The file is already closed by this line.
```

💡 Summary
Use open() to access files.

Understand the difference between w (overwrite) and a (append).

Always close your files, or better yet, just use the with open(...) as f: syntax so Python handles it for you!
