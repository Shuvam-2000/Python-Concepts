# class Attribute
# magic method - it gets called automatically whenver any object is made
# magic methods are used to create attributes or variables of a class

# making a class
class Human:
    def __init__(self, fname, lname, age):  # magic method
        # attributes
        self.first_name = fname
        self.last_name = lname
        self.age = age
    

# obj 1
Shuvam = Human("Shuvam", "Saha", 24)
Shuvam.age = 23
print(Shuvam.first_name, Shuvam.last_name, Shuvam.age)

print()

# obj 2
Riju = Human("Riju", "Saha", 24)
print(Riju.first_name, Riju.last_name, Riju.age)

print("----------------------------")

# making a class
class Man:
    def __init__(self, n, l, a):  # magic method
        # attributes
        self.name = n
        self.title = l
        self.age = a

# obj 1
Man_One = Man("Shuvam", "Saha", 24)
print(Man_One.name, Man_One.title, Man_One.age)

print()

# obj 2
Man_Two = Man("Riju", "Saha", 23)
print(Man_Two.name, Man_Two.title, Man_Two.age)
    