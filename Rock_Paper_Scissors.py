# rock paper scissors game
import random

OPTIONS = ["rock", "paper", "scissors"]
run = True

while run:
    AI = random.choice(OPTIONS)
    player = input("rock, paper or scissors? :")

    if player == AI:
        print(player)
        print(AI)
        print("Draw")
    elif player == OPTIONS[0] and AI == OPTIONS[1]:
        print(player)
        print(AI)
        print("Player lose!")
    elif player == OPTIONS[0] and AI == OPTIONS[2]:
        print(player)
        print(AI)
        print("Player win!")

    elif player == OPTIONS[1] and AI == OPTIONS[0]:
        print(player)
        print(AI)
        print("Player win!")
    elif player == OPTIONS[1] and AI == OPTIONS[2]:
        print(player)
        print(AI)
        print("Player lose!")

    elif player == OPTIONS[2] and AI == OPTIONS[0]:
        print(player)
        print(AI)
        print("Player lose!")
    elif player == OPTIONS[2] and AI == OPTIONS[1]:
        print(player)
        print(AI)
        print("Player win!")

    leave = input("Do you want to rematch?(yes/no):")
    if leave == "yes":
        continue
    else:
        print("Ok, Bye")
        run = False
