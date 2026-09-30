import os

print("="*65)
print(" 🚀 Day 17 Practice: Advanced File Modes ('x' and 'b')")
print("="*65)

file_name = "safe_data.txt"

# Reset: Delete file if it already exists from a previous run
if os.path.exists(file_name):
    os.remove(file_name)

# 1️⃣ Exclusive Creation ('x' mode) - First Attempt
print("\n1️⃣ EXCLUSIVE CREATION ('x' mode) - Attempt 1:")
try:
    with open(file_name, 'x') as f:
        f.write("Secret data stored safely!")
    print(f"   -> ✅ Success! '{file_name}' was created successfully.")
except FileExistsError:
    print(f"   -> ❌ Failed.")

# 2️⃣ Exclusive Creation ('x' mode) - Second Attempt (Preventing Overwrite)
print("\n2️⃣ EXCLUSIVE CREATION ('x' mode) - Attempt 2:")
try:
    with open(file_name, 'x') as f:
        f.write("Trying to overwrite existing data...")
except FileExistsError:
    print("   -> 🛡️ FileExistsError caught! Prevented accidental overwrite of old data.")

# 3️⃣ Reading in Text Mode ('rt')
print("\n3️⃣ READING IN TEXT MODE ('rt'):")
with open(file_name, 'rt') as f:
    text_data = f.read()
print(f"   -> 📄 Output as normal text: {text_data}")

# 4️⃣ Reading in Binary Mode ('rb')
print("\n4️⃣ READING IN BINARY MODE ('rb'):")
with open(file_name, 'rb') as f:
    binary_data = f.read()
print(f"   -> 💾 Output as raw bytes:   {binary_data} (Notice the 'b'!)")

print(" 🎉 Advanced File Operations Executed Successfully!")
