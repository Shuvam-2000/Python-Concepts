# program to print the multiplication table of any number with function

def multiply_table():
    value = int(input("Enter a number : "))
    for i in range(1,11):
        print("{} x {} = {}".format(value, i, i*value))

multiply_table()