import random

def get_user_choice():
    print("Choose Rock, Paper or Scissors:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Enter your choice (1/2/3): ")
    while user_choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2 or 3.")
        user_choice = input("Enter your choice (1/2/3): ")
    return int(user_choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "User"
    else:
        return "Computer"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print("User choice: ", ["Rock", "Paper", "Scissors"][user_choice - 1])
    print("Computer choice: ", ["Rock", "Paper", "Scissors"][computer_choice - 1])
    print("Winner: ", winner)

def play_again():
    print("Do you want to play again? (yes/no)")
    return input("Enter your choice (yes/no): ").lower() == "yes"

def main():
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()
