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


# obj 1
Man_One = Man("Shuvam", "Saha", 24)

# creating new attribute outside class
Man_One.skills = "JavaScript", "Pyhton", "Nodejs", "Reactjs"
print(Man_One.skills)
print(Man_One.first_name, Man_One.skills)

print("------------------------------")

# obj 2
Man_Two = Man("Riju", "Saha", 23)
