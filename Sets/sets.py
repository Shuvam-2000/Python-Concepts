# sets in python

list_1 = [1,5,1,2,3,2,4]

set1 = set(list_1)

# print(set1);

# different operations on set
set1.add(6)
set1.remove(6)

print(set1)

print()

# union of two set - filtering the common values & printing a new set
set_2 = {1,2,3,4,5,6,7}
set_3 = {1,2,3,4}

union = set_2 | set_3

print(union)

# intersection in set - fetching the common values
set_4 = {1,2,3,4,5,6,7}
set_5 = {1,2,3,4}

intersection = set_4 & set_5

print(intersection)

# converting sets to list
set_4 = {1,2,3,4,5,6,7}

Newlist = list(set_4)

print(type(Newlist))
print(Newlist[2])

