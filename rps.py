#rock paper scissors game

import random

while True:
    player_action = input("Enter a choice (rock, paper, scissors): ")
    all_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(all_actions)
    print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")

    if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a tie!")
    elif player_action.lower() == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_action.lower() == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action.lower() == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break



