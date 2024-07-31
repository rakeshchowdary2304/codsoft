import random

def get_user_choice():
    # Prompt user to choose rock, paper, or scissors
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    # Generate a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the choices
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def print_choices(user_choice, computer_choice):
    # Print the choices made by the user and the computer
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def print_result(result):
    # Print the result of the game
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    elif result == "computer":
        print("Computer wins!")

def play_again():
    # Ask user if they want to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'no']:
            return play_again == 'yes'
        else:
            print("Invalid input! Please enter yes or no.")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print_result(result)
        
        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        if not play_again():
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
