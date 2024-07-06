# print the follwoing pattern with nested loop

# *
# * *
# * * *
# * * * *
# * * * * *


for i in range(1,6):
    for x in range(1, i+1):
        print("*" , end="")
    print("")

print()

# printing the pattern in oposite direction
for i in range(6,0,-1):
    for x in range(6, 6-i,-1):
        print("*" , end="")
    print("")