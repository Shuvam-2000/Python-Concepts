# continue statment in python
# example

# continue in for loop
for i in range(1,10):
    if i == 5 or i == 7:
        continue
    print(i)

print()

# continue in while loop
x = int(input("Number : "))

while True:
    if x <= 10:
        if x == 5:
            x+= 1   # to make the loop progress after it breaks out of 5
            continue
    print(x)
    x+=1
    if x > 10:
        break