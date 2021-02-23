import random                   ## get module to generate numbers randomly
import os                       ## get module that will allow to check if file exists

secret=random.randint(1,30)     ##secret number randomly generated
file="guess_best_score.txt"     ##nr of file
tries=0## nr of attempts

if not os.path.exists(file):    # if file doesn't exist
    open(file,"w")
else:                           # if exists open the file
    with open(file,"r") as best_score:
        b=best_score.read()
        best_score.close()

if b=="":                       #if no best score exists
    best=100000000
else:                           #if exists get the value
    best=int(b)

guess=0                         ## zero is never the secret number so it's perfect for initializing

while guess != secret:
    guess = int(input("Insert a guess between 1-30"))
    tries+=1

    if guess==secret:
        print("You got it Magician at the " + str(tries) +" attempt")
        if tries<best:          ## if the nr of attempts is lower than the best score it becomes the high score

            with open(file,"w") as best_score:
                best_score.write(str(tries))
                best_score.close()
        break                   ##exits while cycle

    if guess!=secret:

        if guess>secret:
            print("The secret number is smaller than your attempt")
        else:
            print("the secret number is larger than your attempt")

    if tries>=10:#100:
        print("It looks like too many attempts. Maybe you should rest and try later")
        break                   ##exits while cycle