#Data Types

a = 10
b = 5.7
c = 2+3j
d = True
e = "hello world"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("-------------------------------------------")

#INDEXING

s = "This is Python"
print(s[0])    # 'T' → first character
print(s[5])    # 'i' → sixth character
print(s[-1])   # 'n' → last character
print(s[-6])   # 'P' → sixth from the end

#SLICING

s = "This is Python"
print(s[0:4])     # "This" → characters from index 0 to 3
print(s[5:7])     # "is"   → characters from index 5 to 6
print(s[:4])      # "This" → from start to index 3
print(s[8:])      # "Python" → from index 8 to end
print(s[::2])     # "Ti sPto" → every 2nd character
print(s[::-1])    # "nohtyP si sihT" → reversed string

#Basic String Operation

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
