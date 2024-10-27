from guess_game import play as play_guess
from currency_roulette_game import play as play_currency
from memory_game import play as play_memory
from score import add_score
from utils import screen_cleaner


def start_play():
    """Starts the selected game based on user input."""
    print("Welcome to the Game Center!")
    print("Select a game:")
    print("1. Guess Game")
    print("2. Currency Roulette Game")
    print("3. Memory Game")

    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play (1-3): "))
            if game_choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    difficulty = int(input("Set the difficulty level (1 to 10): "))

    screen_cleaner()  # Clear screen before starting the game

    # Game execution and score management
    if game_choice == 1:
        if play_guess(difficulty):
            add_score(difficulty)
    elif game_choice == 2:
        if play_currency(difficulty):
            add_score(difficulty)
    elif game_choice == 3:
        if play_memory(difficulty):
            add_score(difficulty)


if __name__ == "__main__":
    start_play()
