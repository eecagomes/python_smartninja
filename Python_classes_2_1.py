
#Exercices
#1

continue_conversions="y"
print("Greetings. You have asked for calculator help for distance conversion")

while continue_conversions=="y":
    distance_kms=float(input("Please introduce the distance in kms"))

    miles = distance_kms * 0.621371

    print("the "+ str(distance_kms) +" corresponds to " + str(miles) +" in miles")
    continue_conversions=input("Do you want to do any other conversions?") #choice.lower to force lower case

    if continue_conversions=="n":
        print("You're welcome any time. Take care")
        break
    elif continue_conversions!="y":
        print("Conversions completed. Take care")

#2 Fizzbuzz

n=int(input("Please introduce a number between 1 and 100"))


for i in range(n+1):## n%a n mod a. n mod a is equal to zero when n is divisable by a

    if i>0:
        if i%3==0 and i%5!=0:
            print("buzz")
        if i%5==0 and i%3!=0:
            print("fizz")
        if i%5==0 and i%3==0:
            print("fizzbuzz")
        if i%3!=0 and i%5!=0:
            print(str(i))



#3 string lowercase

string_to_convert_lowercase=input("Write the string to lowercase")

print(string_to_convert_lowercase.lower())





