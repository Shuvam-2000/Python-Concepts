# nested while loop - print the pattern

# *
# * *
# * * *
# * * * *
# * * * * *


line = 1

while line <= 5:
        star = 1
        while star <= line:
                print("*", end="")
                star+= 1
        print("")
        line+= 1


print()

# printing the oposite pattern
line1 = 5

while line1 >= 1:
    star1 = line1
    while star1 >= 1:
        print("*", end="")
        star1 -= 1
    print("")
    line1 -= 1
