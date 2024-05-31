#TASK4
#ROCK, PAPER, SCISSORS

import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    while True:
        again = input("Do you want to play another round? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        if not play_again():
            break
    
    print("Thanks for playing Rock-Paper-Scissors!")

if __name__ == "__main__":
    main()

    print("Thanks for playing Rock-Paper-Scissors!")

if __name__ == "__main__":
    main()
