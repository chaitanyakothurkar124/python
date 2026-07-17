import random

# Number to choice
choices = {
    1: "Scissor",
    0: "Rock",
    -1: "Paper"
}

# Choice to number
reverse_choices = {
    "Scissor": 1,
    "Rock": 0,
    "Paper": -1
}

# Computer chooses randomly
computer = random.choice([-1, 0, 1])

# User input
user = input("Enter your choice (Rock/Paper/Scissor): ").capitalize()

# Validate input
if user not in reverse_choices:
    print("Invalid Choice!")
else:
    user = reverse_choices[user]

    print(f"\nComputer chose: {choices[computer]}")
    print(f"You chose: {choices[user]}\n")

    if computer == user:
        print("🤝 It's a Draw!")

    elif computer == 1 and user == 0:
        print("🎉 You Win!")
    elif computer == 1 and user == -1:
        print("💻 Computer Wins!")

    elif computer == 0 and user == -1:
        print("🎉 You Win!")
    elif computer == 0 and user == 1:
        print("💻 Computer Wins!")

    elif computer == -1 and user == 1:
        print("🎉 You Win!")
    elif computer == -1 and user == 0:
        print("💻 Computer Wins!")