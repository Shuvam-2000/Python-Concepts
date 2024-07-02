# printing the even numbers using while loop

evenNum = int(input("Enter a number between 1 to 10: "))

while evenNum <= 10:
    if evenNum % 2 == 0:  # Check if the number is even
        print(evenNum)  # Print the even number
    evenNum = evenNum + 1  # Increment the number to move to the next number

print("While Loop ends")

