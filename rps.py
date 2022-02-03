#Python RPS Game
import random

#Getting our player input
print("Welcome to Python Rock Paper Scissors")
print("Please choose Rock, Paper, or Scissors (case senstive)")
player_choice = input()

print("You chose " + player_choice)

#Getting the computer options
print("Computer is choosing its option...")
comp_options = ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(comp_options)

#Tie/Win/Lose conditions
if player_choice == comp_choice:
    print("Computer chose " + comp_choice + ", " "It is a tie!")

elif player_choice == "Paper" and comp_choice == "Rock":
    print("Computer chose " + comp_choice + ", " "You won!")

elif player_choice == "Rock" and comp_choice == "Scissors":
    print("Computer chose " + comp_choice + ", " "You won!")

elif player_choice == "Scissors" and comp_choice == "Paper":
    print("Computer chose " + comp_choice + ", " "You won!")

elif player_choice == "Rock" and comp_choice == "Paper":
    print("Computer chose " + comp_choice + ", " "You lost!")

elif player_choice == "Scissors" and comp_choice == "Rock":
    print("Computer chose " + comp_choice + ", " "You lost!")

elif player_choice == "Paper" and comp_choice == "Scissors":
    print("Computer chose " + comp_choice + ", " "You lost!")

input("Thanks for playing, press ENTER to close!")