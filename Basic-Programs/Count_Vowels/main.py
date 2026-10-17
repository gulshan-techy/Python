
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
print("Total i:", i)
print("Total o:", o)
print("Total u:", u)
print("Total vowels:", a + e + i + o + u)
