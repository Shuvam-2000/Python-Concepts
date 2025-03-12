# filter function in python

people_data = [("Shuvam", 23), 
                ("Riju", 24), 
                ("Shuva", 43), 
                ("Ri", 47)
              ]

new_list = list(filter(lambda person: person[1] < 30, people_data))

print(new_list)