# args in python
# example

def add(num1, num2):
    result = num1 + num2
    print(result)

add(2,4)

# args(helps in giving unlimited argumnet)
def add_3(*num):
    result = 0
    for i in num:
        result = result + i
    print(result)

add_3(2,4,6,8,2,4,6,8)
