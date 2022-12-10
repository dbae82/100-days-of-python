from random import choice
from art import logo, vs
from game_data import data
from os import system


def clear(): return system('clear')


def rand_account(): return choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)
    score = 0
    is_game_over = False
    account_a = rand_account()
    account_b = rand_account()

    while not is_game_over:
        account_a = account_b
        account_b = rand_account()

        while account_a == account_b:
            account_b = rand_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


while input("Do you want to play a game of Higher or Lower? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
