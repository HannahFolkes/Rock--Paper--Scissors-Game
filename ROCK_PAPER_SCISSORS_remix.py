# Python Game: Hannah's SPECIAL ROCK, PAPER, SCISSORS game
# Completion Date: June 2026

import pygame

import random
possible_actions = ["ROCK", "PAPER", "SCISSORS", "CAKE"]



# Opening Console Prompts
print("Welcome to Hannah's SPECIAL ROCK, PAPER, SCISSORS game.")
print()
print("This is a one player game where you have the opporunity to pratice your decision making skills agansit the COMPUTER.")
print("Unlike the standard rock, paper, scissors game, Hannah's verison includes a fourth option called CAKE.")
print()
print("READY TO HAVE SOME FUN!")
print() 

user_action = input ("Enter a choice (ROCK, PAPER, SCISSORS, CAKE): ").upper()
computer_action = random.choice(possible_actions)
print(f"You chose {user_action}, computer chose {computer_action}\n") #Displays game options

if user_action == computer_action: #DEFAULT CASE - GAME TIE (When both players chose the same option)
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "ROCK": #USER ACTION 1 - ROCK 
     if computer_action == "SCISSORS": 
          print("ROCK smashed CAKE into a MILLION PIECES! You win!")    
     else: 
           print("PAPER covers ROCK. You lose!")
elif user_action == "PAPER": #USER ACTION 2 - PAPER
     if computer_action == "ROCK":
         print("PAPER cover ROCK! You win!")
     elif computer_action=="CAKE":
          print("CAKE fell on top of PAPER and got the PAPER soggy! You win!")
     else: 
          print("SCISSORS cuts PAPER! You lose.")
elif user_action == "SCISSORS": #USER ACTION 3 - SCISSORS
    if computer_action == "PAPER": 
         print("SCISSORS cuts PAPER! You win!")
    elif computer_action == "CAKE": 
         print("SCISSORS cuts CAKE! You lose.")
    else: 
         print("ROCK smashes SCISSORS! You lose.")
elif user_action == "CAKE": #USER ACTION 4 [FINAL] - CAKE
     if computer_action == "PAPER": 
          print("CAKE feel on top of PAPER and got the PAPER soggy! You win!")
     elif computer_action == "SCISSORS":
          print("SCISSORS cuts CAKE! You lose.")
     else: 
          print("ROCK smashed CAKE into a MILLION PIECES! You lose.")
