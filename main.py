import random

def game(user_action):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("Computer's action: " + computer_action)
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Paper covers rock! You lose.")
        else:
            print("Rock smashes scissors! You win!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors. You lose.")
    else:
        print("Invalid choice.")

    return user_action
    

def play_game():
    while True:
        print("Welcome to play: ROCK PAPER SCISSORS")
        user_action = input("Enter a choice (rock, paper or scissors): ")

        if user_action not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue
        
        game(user_action)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    play_game()




