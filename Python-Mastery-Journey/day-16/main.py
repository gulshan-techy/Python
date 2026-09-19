print(" 🚀 Day 16 Practice: File Handling (Read, Write, Append)")
file_name = "practice_file.txt"

# 1. Writing to a file ('w' mode)
print("\n 1. WRITING TO A FILE ('w' mode):")
with open(file_name, 'w') as f:
    f.write("Hello! This is the very first line.\n")
print(f"Created '{file_name}' and overwrote existing data.")

# 2.  Reading from the file ('r' mode)
print("\n 2. READING THE FILE ('r' mode):")
with open(file_name, 'r') as f:
    content = f.read()
print("Current Content:")
print(f"      {content.strip()}")

# 3. Appending to the file ('a' mode)
print("\n 3. APPENDING TO THE FILE ('a' mode):")
with open(file_name, 'a') as f:
    f.write("This is the second line, added using append!\n")
print("Appended new data without erasing the old text.")

# 4. Reading the updated file
print("\n 4. READING THE UPDATED FILE:")
with open(file_name, 'r') as f:
    updated_content = f.read()
print("Updated Content:")
print(updated_content)
print("\n 🎉 Operations Successful!")
