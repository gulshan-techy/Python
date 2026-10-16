num = int(input("Enter a number to find the square root: "))
if num < 0:
    print("Square root of negative numbers is not defined in real numbers.")
    exit()
for i in range(1, num+1):
    for j in range(i+1):
        if i == j and i*j == num:
            print("Square Root of your given Number" , num, "is: ", i)
            break
    else:
        continue
    break
else:
    print("No exact square root found for", num)    
