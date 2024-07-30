# lists in python
# example

list_name = ["Shuvam Saha", "Riju Saha"]

print(type(list_name))

print()

# making nested lists
marks_info = ["India", [90,91,92], [80,81,82], [70,71,72], 23, "Shuvam"]

print(marks_info)

print()

# combining two lists
list_combined = list_name + marks_info

print(list_combined)

print()

# make a list which has all the numbers from 0 to 100
num = list(range(1,101,2))

print(num)

print()

# storing each element of a string in a list
text = "My Name Is Shuvam Saha"

convertToList = list("My Name Is Shuvam Saha")

print(convertToList)

print()

# know the length of any list
lengthOfList = (len(convertToList))

print(lengthOfList)