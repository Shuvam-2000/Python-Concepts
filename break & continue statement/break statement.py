# break statement in python example
# example

# break statement in for loop 
for i in range(1,20):
    if i == 5:
        break
    print(i) 

print()

# break statement in while loop
x = int(input("Number : "))

while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1