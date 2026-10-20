# Program to print Fibonacci Series

n = int(input("Enter how many terms you want: "))

# First two terms
a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
