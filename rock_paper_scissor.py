import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the result of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Runs the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice not in ["rock", "paper", "scissors", "exit"]:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        if user_choice == "exit":
            print("Thanks for playing!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score -> You: {user_score}, Computer: {computer_score}")

# Start the game
play_game()
