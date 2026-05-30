# so i have to create a game of rock papers and scisors, where the user has to play against the computer. 
# the computer will randomly select rock, paper or scissors and the user will have to input their choice. 
# then we will compare the choices and determine the winner.

import random

choices = ["rock", "paper", "scissors"]

print("Welcome to the rock paper scissors game!")
print("The rules are simple : rock beats scissors, scissors beats paper and paper beats rock.")
print("You will be playing against the computer. The computer will randomly select rock, paper or scissors and you will have to input your choice. Then we will compare the choices and determine the winner.")
print("Let's start the game!")

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper or scissors) : ")

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper or scissors.")
        continue

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("Congratulations! You win!")
    else:
        print("Sorry! The computer wins!")

    play_again = input("Do you want to play again? (yes or no) : ")
    if play_again in ("no","nope","nah","no thanks","no thank you"):
        print("Thank you for playing! Goodbye!")
        break
    elif play_again in ("yes","yeah","yup","sure","of course","why not"):
        continue
    else:        
        print("Invalid input. conitinuing the game.")