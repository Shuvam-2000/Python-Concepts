# class Attribute
# magic method - it gets called automatically whenver any object is made
# magic methods are used to create attributes or variables of a class

# making a class
class Man:
    def __init__(self, f, l, a):  # magic method
        # attributes
        self.first_name = f
        self.last_name = l
        self.age = a

    def full_name(self):
        print(
            f" Hello My Name is {self.first_name} {self.last_name} and I am {self.age} years old")
    
    def update_age(self, newAge):
        self.age = newAge


# obj 1
Man_One = Man("Shuvam", "Saha", 24)
Man_One.update_age(24)
Man_One.full_name()

print("------------------------------")

# obj 2
Man_Two = Man("Riju", "Saha", 23)
Man_Two.full_name()
