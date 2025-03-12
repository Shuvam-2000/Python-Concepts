# class Attribute vs object attribute

# object attribute
# if any attribute is created using self than it can't be accesed without obj

# class attribute
# if any varibale is created without self it can be accesed without obj direclty
# through class

# making a class
class Man:

    # class attribute
    country = "India"
    def __init__(self, f, l, a):  # magic method
        # object attributes
        self.first_name = f
        self.last_name = l
        self.age = a


# accesing value with the class
print(Man.country)

# # obj 1
# Man_One = Man("Shuvam", "Saha", 24)
# Man_One.country = "United States"
# print(Man_One.country)

# print("------------------------------")

# # obj 2
# Man_Two = Man("Riju", "Saha", 23)
# print(Man_Two.country)
