# map function in python

people_data = [("Shuvam", 23), 
                ("Riju", 24), 
                ("Shuva", 43), 
                ("Ri", 47)
              ]

# map function converts to list
new_list = list(map(lambda person: person[0], people_data))

print(new_list)