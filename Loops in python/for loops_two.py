# print all the even numbers between 1 and 10 using for loop

print("The even numbers between 1 and 10 are : ".title())

print();

for i in range(2,11, 2):
    # if i % 2 == 0:  # checking the even number by dividing with 2
    #     print("The number is {} even".format(i));
    # else:
    #     print("The number is {} odd".format(i));


    # can also be done in a simple way
    print("The number {} is even".format(i))

print()

# print the table of 2 

print("The Table Of 2 : ")

for i in range(1,11):
    print(" 2 x {} = {}".format(i, 2*i))
