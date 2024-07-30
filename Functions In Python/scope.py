# scope of variable
# example

# global variable
num = 1
var0 = "global"

def hello(name,age):
    # local varibale
    message = "good morning!"
    print(message)
    print(name,age)

hello("Shuvam", 23)


def variable():
    var1 = "local var 1"

def variable2():
    var2 = "local var 2"

variable()
variable2()
