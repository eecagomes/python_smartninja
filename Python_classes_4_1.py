# import libraries
import os  # will use to check if file exists
import random  # will use to generate random nrs
import datetime  # will us eto get the current date and time
import json  # will use to load and "dump" the data in/from the txt file

file_name = "guess_best_score.txt"

if not os.path.exists(file_name):  # if txt file doesn't exist it will create a new one
    with open(file_name, "w") as guess_best_score:
        guess_best_score.close()

with open(file_name, "r") as guess_best_score:  # if file already exists we'll get the information
    try:
        scores_list = json.loads(guess_best_score.read())  # json will convert the types from the txt file to the vector

    except:  # if error occurs due to file being completely empty
        scores_list = []
guess_best_score.close()

# initiating variables
tries = 0
min = 1
max = 30
player_name = str(input("Please insert your name"))
secret = random.randint(1, 30)
guesses = []

while True:
    tries += 1
    guess = int(input("Please choose a number between " + str(min) + " and " + str(max)))
    guesses.append(guess)

    if guess > 30 or guess < 1:
        print("Guess number must be between" + str(min) + " and " + str(max) + ".Please try again")

    else:

        if guess > secret:
            print("Secret number is lower than guess")

        if guess < secret:
            print("secret number is higher than guess ")

        if guess == secret:
            current_date = datetime.datetime.now()
            best = {"Name": str(player_name), "Date": str(current_date), "Attempts": str(tries),
                    "Guesses": str(guesses)}
            scores_list.append(best)

            with open(file_name, "w") as guess_best_score:
                guess_best_score.write(json.dumps(scores_list))  # writing on the txt file using json.dumps
                guess_best_score.close()
            print("Got it at the " + str(tries) + " attempts")

            break
