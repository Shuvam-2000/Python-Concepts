# unpacking of lists
# example

name = ["Shuvam Saha", "Riju Saha", "Python"]

# storing all the items in the list in different variables
first, second, third = name[0:3]
first, second = name[0:2]

print(first, second, third)
print()
print(first, second)

name2 = ["Shuvam Saha", "Riju Saha", "Python", 1, 2, 3, "India"]

first, second, third, *list2, fourth = name2

print(first, second, third, *list2, fourth)
print(*list2)

