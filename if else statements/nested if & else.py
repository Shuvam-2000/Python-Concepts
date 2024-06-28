# nested if else statement in python
# example 

# program to guess numbers between 1 and 20 while the numbers should not be higher or lower than 15

answer = 15 

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer: 
    if guess < answer: 
        print("Please guess higher")
    else:    #guess must be greater than answer 
        print("Please guess lower")
    guess = int(input())
    if guess == answer: 
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")    
else:
    print("You got it first time")