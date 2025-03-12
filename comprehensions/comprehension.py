# comprehensions in python

people_data = [("Shuvam", 23), 
                ("Riju", 24), 
                ("Shuva", 43), 
                ("Ri", 47)]

# syntax of a comprehension 
# new_names = [statement for x in list]

# comprehension
new_names = [person[1] for person in people_data]

print(new_names)

print()

# filter function
new_list = list(filter(lambda person: person[1] < 30, people_data))

print(new_list)

print()

# syntax for using comprehension in filter function
# list_1 = [statement for x in list condition]

# using comprehension in filter function
list_1 = [person for person in people_data if person[1] < 30]

print(list_1)
