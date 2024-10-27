import random
import time


def generate_sequence(difficulty):
    return [random.randint(1, 100) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    while True:
        try:
            user_input = input(f"Enter {difficulty} numbers (space-separated): ")
            user_list = list(map(int, user_input.split()))
            if len(user_list) == difficulty:
                return user_list
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize this sequence:")
    print(sequence)

    time.sleep(0.7)
    print("\033[H\033[J", end="")  # Clear the console

    user_list = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_list):
        print("Well Done!! You remembered the sequence correctly.")
        return True
    else:
        print(f"Sorry.. the correct sequence was {sequence}. Better luck next time!")
        return False
