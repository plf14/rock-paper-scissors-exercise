# game.py

import random
ComputerChoice = random.choice(['rock', 'paper', 'scissors'])

print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

UserChoice = input("Ok, rock, paper, scissors:  ")
ValidOptions = ['rock', 'paper', 'scissors']
print("You chose:  ", UserChoice)
if UserChoice.lower() not in ValidOptions:
    print("-------------------")
    print("Your choice is invalid.  Please play again.")
    exit()
print("The computer chose:  ", ComputerChoice.title())
print("-------------------")

if ComputerChoice == UserChoice.lower():
    print("It's a tie!")
elif  UserChoice.lower() == 'rock':
    if ComputerChoice == 'scissors':
        print("You win!")
    elif ComputerChoice == 'paper':
        print("You lose!")
elif  UserChoice.lower() == 'paper':
    if ComputerChoice == 'rock':
        print("You win!")
    elif ComputerChoice == 'scissors':
        print("You lose!")
elif  UserChoice.lower() == 'scissors':
    if ComputerChoice == 'paper':
        print("You win!")
    elif ComputerChoice == 'rock':
        print("You lose!")

print("-------------------")
print("Thanks for playing. Please play again!")