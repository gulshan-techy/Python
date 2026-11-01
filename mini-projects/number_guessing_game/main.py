import random

computer_num = random.randint(0, 100)
max_attempts = 15

print("Welcome to Number Guessing Game!")
print(f"You have maximum {max_attempts} attempts to guess the number between 0 and 100.")

for i in range(max_attempts):

    print(f"\nAttempts remaining: {max_attempts - i}")

    try:
        user_num = int(input("Guess The Number: "))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    if user_num < 0 or user_num > 100:
        print("Please enter a number between 0 and 100.")
        continue

    if user_num == computer_num:
        print(f"Congratulations! You guessed the correct number: {computer_num}")
        break

    elif computer_num > user_num:
        print("Number is Higher, Try Again!")

    else:
        print("Number is Lower, Try Again!")

else:
    print("\nGame Over! You have used all your attempts.")
    print(f"The correct number was: {computer_num}")
