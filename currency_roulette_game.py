import random
import requests

def get_money_interval(difficulty):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    exchange_rate = data['rates']['ILS']

    secret_value = random.randint(1, 100)
    correct_value = secret_value * exchange_rate
    allowed_difference = 10 - difficulty

    return correct_value, allowed_difference

def get_guess_from_user():
    while True:
        try:
            guess = float(input("Guess the value in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def compare_results(correct_value, allowed_difference, user_guess):
    return (correct_value - allowed_difference) <= user_guess <= (correct_value + allowed_difference)

def play(difficulty):
    correct_value, allowed_difference = get_money_interval(difficulty)
    print(
        f"The correct value is between {correct_value - allowed_difference:.2f} and {correct_value + allowed_difference:.2f} ILS.")

    user_guess = get_guess_from_user()

    if compare_results(correct_value, allowed_difference, user_guess):
        print("GOOD!!! Your guess is within the acceptable range.")
        return True
    else:
        print(f"Sorry.. the correct value was {correct_value:.2f} ILS. Better luck next time!")
        return False
