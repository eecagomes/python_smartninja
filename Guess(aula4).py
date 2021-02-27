import random  ## get module to generate numbers randomly
import os  ## get module that will allow to check if file exists
import json  ## json library
import datetime  ## data actual

secret = random.randint(1, 30)  ##secret number randomly generated
file = "guess_best_score.txt"  ##nr of file
tries = 0  ## nr of attempts

if not os.path.exists(file):  # if file doesn't exist
    with open(file, "w") as best_score:
        best_score.write([])
    best_score.close()

else:  # if exists open the file
    with open(file, "r") as best_score:
        lista_scores = json.loads(best_score.read())  ## json loads interprets all the values automatically
        lista_scores.sort()
        best_score.close()

guess = 0  ## zero is never the secret number so it's perfect for initializing
name=str(input("What is your name reader of minds?"))
while guess != secret:

    guess = int(input("Insert a guess between 1-30"))
    tries += 1

    if guess == secret:
        data_actual = datetime.datetime.now()  # data actual
        print("You got it Magician at the " + str(tries) + " attempt")
        lista_scores.append({"tentativas": tries, "data": str(data_actual), "name":name})  ## dictionary com as scores
        ##lista_scores.sort()

        with open(file, "w") as best_score:
            best_score.write(
                json.dumps(lista_scores))  ##json interprets automatically the type of variable when writing
            best_score.close()

    if guess != secret:

        if guess > secret:
            print("The secret number is smaller than your attempt")
        else:
            print("the secret number is larger than your attempt")

    if tries >= 100:  # 100:
        print("It looks like too many attempts. Maybe you should rest and try later")
        break  ##exits while cycle
