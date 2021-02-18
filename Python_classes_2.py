import random #import package random

secret=random.randint(1,42)

guess=int(input("Please select a number between 1-42"))

for x in range(5):#for cycle range(5) goes from 0 to 4. 5 is inclusively. Step can be placed in range function

    #while guess!= secret:# can use break to get out of loop
    if guess==secret:
        print("Got it")
        break
    elif guess<secret:
        print("Mais para cima")
    elif guess>secret:
        print("Mais para baixo")
    else:
        print("you missed it. Try again")
