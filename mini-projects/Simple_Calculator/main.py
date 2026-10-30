a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

calc = input("Enter the operation sign (+, -, *, /): ")

result = 0

if calc == "+":
    result += a+b
elif calc == "-":
    result += a-b
elif calc == "*":
    result += a*b
elif calc == "/":
    result += a/b
else: 
    print("Please Enter the right operation sign")

print(result)
