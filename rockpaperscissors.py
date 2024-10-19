import random
while True:
    user = input("enter rock paper or scissors : ::: ...:...:...: ")
    scriptchc = ["rock", "paper", "scissors"]
    computer = random.choice(scriptchc)
    if user == computer:
        print("tie")
    elif user == "rock":
        if computer == "scissors":
            print(user," beats ",computer)
        else:
            print(computer,"beats ",user)
    elif user == "paper":
        if computer == "rock":
            print(user," beats ",computer)
        else:
            print(computer," beats ",user)
    elif user == "scissors":
        if computer == "paper":
            print(user," beats ",computer)
        else:
            print(computer," beats ",user)
    