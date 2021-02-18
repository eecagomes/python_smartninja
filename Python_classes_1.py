

# homework1

mood = input("Please input your emotional stage")

if mood =="happy":
    print("It is great to see you happy!")
elif mood =="nervous":
    print("Take a deep breath 3 times")
elif mood =="sad":
    print("Don't worry. Be Happy!")
elif mood =="relaxed":
    print("You're a Zen Master")
elif mood =="excited":
    print("Please do some taichi to relax")
else:
    print("Don't know what is that emotional stage")


#homework 2 perfect number

secret = 3
guess =int(input("Please guess the number 1-10"))

if guess == secret:
    print("You're a winner")
else:
    print("you lost. Better Luck next time")

#Homework 3

first_nr=int(input("Introduce thr 1st whole number"))
second_nr=int(input("Introduce the 2nd whole number"))
operation=str(input("Please introduce the operation you want: '+';'-';'*';'/'"))

if operation != '+' and operation != '-' and operation != '*' and operation != '/':
    print("no suitable operators selected. Program terminated.")
    exit() #quits program
else:
    if operation =='+':
        result=first_nr+second_nr
    if operation =='-':
        result=first_nr-second_nr
    if operation =='*':
        result=first_nr*second_nr
    if operation =='/':
        result=first_nr/second_nr

print("Result is " + str(result))

