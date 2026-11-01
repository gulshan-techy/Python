print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100.")
print("Computer will try to guess your number.")

low = 1
high = 100

for i in range(7):

    comp_guess = (low + high) // 2

    print(f"\nAttempt {i + 1}: Is your number {comp_guess}?")

    user_reply = input("Enter (correct/lower/higher): ").strip().lower()

    if user_reply == "correct":
        print("Congratulations! I guessed your number!")
        print(f"I guessed it in {i + 1} attempts.")
        break

    elif user_reply == "lower":
        high = comp_guess - 1

    elif user_reply == "higher":
        low = comp_guess + 1

    else:
        print("Invalid input! Please enter correct, lower, or higher.")
        continue

    if low > high:
        print("Your responses are inconsistent! Please check your answers.")
        break

else:
    print("\nI couldn't guess your number within 7 attempts.")
