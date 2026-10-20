num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    print(f"Divisors of {num} are: {divisors}")
