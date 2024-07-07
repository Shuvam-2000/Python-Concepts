# functions in python
# example


def basic():
    print("Hi")

basic()


def say_hello():
    name = "Shuvam"
    a = int(input("Enter a number less than 10: "))
    if a >= 10:
        print("Number is 10 or greater")
    else:
        while a < 10:
            print("Hello {}".format(name))
            a += 1

say_hello()
