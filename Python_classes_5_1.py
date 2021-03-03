# import libraries
import random  # will use to generate random nrs
from functions_hw import run_game, save_data, check_file_exists  # will use the functions_hw for calling the functions

file_name = "guess_best_score.txt"

check_file_exists(file_name)  # checks if file exists

player_name = str(input("Please insert your name"))
difficulty = str(input("Please select between easy and hard difficulty"))
min = 1
max = 30
secret = random.randint(min, max)
tries = 0
guesses = []
status = True

while status:
    tries += 1
    status, guesses = run_game(difficulty, guesses, tries, secret, min, max)

if not status:  # after getting it right
    save_data(file_name, player_name, tries, guesses)
