# magic methods

# making a class
class Man:

    def __init__(self, f, l, a):  # magic method
        # object attributes
        self.first_name = f
        self.last_name = l  # private attribute
        self.age = a

    def __str__(self):
        return f"{self.first_name} is a Human Object, and age of this Human is {self.age}"


# obj 1
Man_One = Man("Shuvam", "Saha", 24)
print(Man_One)
