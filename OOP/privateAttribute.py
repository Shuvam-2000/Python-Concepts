# private attribute - cannot be accesed outside class. To access a 
# private attribute its needed to be defined witha function inside the class

# making a class
class Man:

    def __init__(self, f, l, a):  # magic method
        # object attributes
        self.first_name = f
        self.last_name = l 
        self.__age = a # private attribute
    
    def get_age(self):
        print(self.__age)

# obj 1 
Man_One = Man("Shuvam", "Saha", 24)

# accesing the private attribute 
Man_One.get_age()