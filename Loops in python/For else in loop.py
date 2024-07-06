# using else statement in loop
# example

# program to guess even no and odd number. If the user gives even number the program
# ends after a no of attempts when there is a minimum money balance

print("Identify the odd numbers :")
money = 10

for number in range(10):
    num = int(input("Enter odd Number: "))
    if num > 10:
        print("The number is out of range")
    elif num %2 == 0:
        print("The number is even !!")
    else:
        print("The number is odd. You guessed it right in Rs {}".format(money))
        break

    money -= 1
    if money == 5:
        print("Low Balance ! No more Attempts Allowed")
        break