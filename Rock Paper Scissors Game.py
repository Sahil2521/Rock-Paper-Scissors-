import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
    print("computer :",computer)
    print("player :",player)
    if player == computer:
        print("Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("You Lose")
        elif computer == "scissors":
            print("You Win")
    elif player == "paper":
        if computer == "scissors":
            print("You Lose")
        elif computer == "rock":
            print("You Win")
    elif player == "scissors":
        if computer == "rock":
            print("You Lose")
        elif computer == "paper":
            print("You Win")
    
    play_again = input("Want to play again? (yes/no):").lower()
    if play_again != "yes":
        break

print("Bye!!")    

