import random

user = input("Enter your choice (rock, paper, scissors): ").lower()

choices = ["rock", "paper", "scissors"]

if user not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")

else:
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Draw! You both chose:", user)

    elif user == "paper" and computer == "rock":
        print("You Won!")

    elif user == "scissors" and computer == "paper":
        print("You Won!")

    elif user == "rock" and computer == "scissors":
        print("You Won!")

    else:
        print("Computer Won!")












