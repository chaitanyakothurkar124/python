
import random

dict = {
    1: "scissor",
    0: "Rock",
    -1: "paper"
}

reversed_dict = {
    "scissor": 1,
    "Rock": 0,
    "paper": -1
}

computer = random.choice([-1, 0, 1])

user = input("Enter your choice (Rock/paper/scissor): ")

user = reversed_dict[user]   # Convert string to number

print("Computer chose:", dict[computer])

if computer == 1 and user == 0:
    print("User wins")
elif computer == 1 and user == -1:
    print("Computer wins")
elif computer == 0 and user == -1:
    print("User wins")
elif computer == 0 and user == 1:
    print("Computer wins")
elif computer == -1 and user == 0:
    print("Computer wins")
elif computer == -1 and user == 1:
    print("User wins")
elif computer == user:
    print("It's a Draw")
else:
    print("Something went wrong")