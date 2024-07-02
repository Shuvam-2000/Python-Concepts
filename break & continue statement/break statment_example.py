# program to guess the given number in variable using while loop

num = 50
attempt = 1


print("Guess a number between 1 and 50 :- ")

guess = int(input("Enter Number : "))

while guess != num:
    if guess > num:
        print("Please guess lower")
    elif guess < num:
        print("Please guess higher")
    guess = int(input("Please Try again : "))
    attempt += 1
    if attempt == 6:
        print("Attempts Ended Game Over You Loose ||")
        break

if guess == num:
    print("You guessed it right in {} attempts".format(attempt))
