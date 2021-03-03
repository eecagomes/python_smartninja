# import libraries
import os  # will use to check if file exists
import datetime  # will us eto get the current date and time
import json  # will use to load and "dump" the data in/from the txt file


def run_game(difficulty, guesses, tries, secret, min, max):
    guess = int(input("Please choose a number between " + str(min) + " and " + str(max)))
    guesses.append(guess)

    if guess > max or guess < min:
        print("Guess number must be between" + str(min) + " and " + str(max) + ".Please try again")
        quit()
    else:
        if difficulty == "easy" and guess != secret:

            if guess > secret:
                print("Secret number is lower than guess")

            if guess < secret:
                print("secret number is higher than guess")

            return True, guesses

        if difficulty == "hard" and guess != secret:
            print("Wrong number")
            return True, guesses

        if guess == secret:
            print("Got it at the " + str(tries) + " attempts")
            return False, guesses


def save_data(file_name, player_name, tries, guesses):
    current_date = datetime.datetime.now()
    best = {"Name": str(player_name), "Date": str(current_date), "Attempts": str(tries),
            "Guesses": str(guesses)}
    scores_list = open_data(file_name)  # before appending needs to open
    scores_list.append(best)

    with open(file_name, "w") as guess_best_score:
        guess_best_score.write(json.dumps(scores_list))  # writing on the txt file using json.dumps
        guess_best_score.close()


def open_data(file_name):
    with open(file_name, "r") as guess_best_score:  # if file already exists we'll get the information
        try:
            scores_list = json.loads(
                guess_best_score.read())  # json will convert the types from the txt file to the vector

        except:  # if error occurs due to file being completely empty
            scores_list = []
    guess_best_score.close()

    return scores_list


def check_file_exists(file_name):
    if not os.path.exists(file_name):  # if txt file doesn't exist it will create a new one
        with open(file_name, "w") as guess_best_score:
            guess_best_score.close()
