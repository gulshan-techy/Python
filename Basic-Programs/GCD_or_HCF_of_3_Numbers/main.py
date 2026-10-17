num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

smaller = 0
if num1 < num2 and num1 < num3:
    smaller = num1
elif num2 < num1 and num2 < num3:
    smaller = num2
else:
    smaller = num3

hcf = 0

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        hcf = i   
          
print("HCF of the three numbers is:", hcf)
