import random

#   gives you the start
action = input("Enter a choice (rock, paper, scissors): \n")

#   gives the choices
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"\nYou chose {action}, computer chose {computer_choice}.\n")

#   tales the choices and then determines the winner
if action == computer_choice:
    print(f"Both players selected {action}. It's a tie!")
elif action == "rock":

    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif action == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif action == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        
