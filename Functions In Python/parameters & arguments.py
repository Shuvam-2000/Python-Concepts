# paramters & arguments in python

def add(num1 , num2):
    return (num1 + num2)

print(add(2,4))

# num1 & num2 are paramters passed in the add fucntion
# which will return the addition of num1 & num2

# 2,4 are arguments passed in the add fucntion for the arguments
# num1 & num2 which will add the values and give the result 6 

print()

def multiply_table(value):
    for i in range(1,11):
        print("{} x {} = {}".format(value, i, i*value))

multiply_table(2)