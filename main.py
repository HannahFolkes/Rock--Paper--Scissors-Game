import random
#Console Prompts 
user_action = input("Enter a choice (rock, paper, scissors, cake): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#Game Logic (Choices)
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")      
elif user_action == "cake":
        if computer_action == "paper":
          print ("Cake ruins paper! You win!")
        else: 
          print ("Rock smashes cake! You lose.")
          
elif user_action == "cake":
          if computer_action == "scisscors":
            print ("Scissors cuts cake! You lose.")
          else: 
            print ("Cake can't destory scissors. You lose!")

      