# here we need to make a number guessing game where the user has to guess a number between 1 and 100. 

# This is my attempt at making the game, its basic, no score or anything.
# import random

# print("Welcome to the number guessing game!")
# print("I have selected a number between 1 and 100. Can you guess it?")


# b = random.randint(1, 100)
# a = int(input("Enter your guess : "))


# while a != b:
#     a = int(input("Enter your guess : "))
#     if a < b:
#         print("Your guess is a little low. Try again.")
#     elif a > b:
#         print("Your guess is a little high. Try again.")
#     else:
#         print("Congratulations! You guessed the number right.")
#         break


# This one is a little more advanced, it keeps track of the number of attempts and gives you a score based on how many attempts you took to guess the number.

import random


com = random.randint(1, 100)
score = 0
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    a = int(input("Enter your guess : "))
    score += 1
    if a < com:
        print("Your guess is a little low. Try again.")
    elif a > com:
        print("Your guess is a little high. Try again.")
    else:
        print(f"Congratulations! You guessed the number right in {score} attempts.")
        break
    