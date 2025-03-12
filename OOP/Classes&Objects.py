# class - blueprint of creating a new object
# Object - instance of class

# class: Human
# object: Shuvam, Riju

# property/feature - Attribute
# function - method

# making a class
class Human:
    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")

# class Human store in object Shuvam
Shuvam = Human()  

# using the functions in the class in the object Shuvam
Shuvam.eat()
Shuvam.walk()

# new object for the Human class
Riju = Human()

# using the functions
Riju.walk()