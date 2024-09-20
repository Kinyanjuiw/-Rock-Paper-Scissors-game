#Rock beats Scissors.
#Scissors beat Paper.
#Paper beats Rock.
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    # Ask the user for their choice
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

    # Check if the user wants to quit the game
    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    # Validate user input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result + "\n")
