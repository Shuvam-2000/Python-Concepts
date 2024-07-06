# nested loop example
# print tables from 2 to 5


for x in range(2,6):
    print("Table of {}".format(x))
    for i in range(1, 11):
        print("{} x {} = {}".format(x,i,x*i))
    print("----------------------")
