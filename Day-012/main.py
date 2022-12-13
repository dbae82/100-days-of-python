# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
import os

def clear(): return os.system('clear')

def play_game():
    random_number = random.randint(1, 100)
    chances = 0
    is_game_over = False

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        chances = 10
    elif difficulty == 'hard':
        chances = 5
    else:
        print("C'mon man! There are only two options. Game over.")
        is_game_over = True

    while not is_game_over:
        print(f"You have {chances} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == random_number:
          print(f"You got it! The answer was {player_guess}.")
          is_game_over = True
        if player_guess > random_number:
          print("Too high.\nGuess again.")
          chances -= 1
        if player_guess < random_number:
          print("Too low.\nGuess again.")
          chances -= 1
        if chances == 0:
          print("You've run out of guesses, you lose.")
          is_game_over = True

while input("Do you want to play a game of Number Guess? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
