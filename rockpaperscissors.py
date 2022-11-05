#rockpaperscissors

import random

use_score = 0
computer_score = 0
user_wins = 0
computer_wins = 0
run = True

options = ["rock", "paper", "scissors"]

while run:
    user_input = input("Type rock/paper/scissore OR Q to quit: ").lower()
    if user_input == "Q":
        run = False
        break

    if user_input  not in options:
        continue

    random_number = random.randint(0, 2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("The Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "rock" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "scissors":
        print("You lost!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

    print("You won", user_wins, "times!")
    print("The computer won", computer_wins, "times!")
    print("Goodbye!")        


