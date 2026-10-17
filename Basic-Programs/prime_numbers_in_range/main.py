num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

count = []

for i in range(num1, num2 + 1):
    x = 0
    for j in range(1, i+1):
        if i % j == 0:
            x += 1
    if x == 2:
        count.append(i)
    else:
        continue
            
print(count)
len = len(count)
print(f"Total Prime Numbers between {num1} and {num2}: {len}")
