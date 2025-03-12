# class Attribute
# magic method - it gets called automatically whenver any object is made
# magic methods are used to create attributes or variables of a class

# making a class
class Human:
    def __init__(self, name, age):  # magic method
        self.name = name  # attributes
        self.age = age

    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")


# class Human store in objects
Shuvam = Human("Shuvam", 24)
Riju = Human("Riju", 23)

print(Shuvam.name)
print(Riju.name)
