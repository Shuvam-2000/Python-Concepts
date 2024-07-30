# Tuples In Python
# Example

student_data = ("Shuvam", "Riju", 23, "Coding")

print(student_data)
print(type(student_data))

print("---------------------")

# operations on tuple
tuple_no = (1,2,3)
tuple_no2 = (4,5)

# concatenating a tuple
concat = tuple_no + tuple_no2

print(concat)

# converting list to tuple
listToConvert = [1,2,3,4]

tuple(listToConvert)

# accesing item form tuple
tuple_data = ("Shuvam", "Riju", 23, "Coding")

items = tuple_data[0:3]

print(items[2]*3)

# unpacking of tuple
unpack_tuple = (1,2,3)

x , y, z = unpack_tuple

print(x, y, z)

# finding a item in a tuple
if 3 in unpack_tuple:
    print("yes")
else:
    print("No")