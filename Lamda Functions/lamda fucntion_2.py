# using the lamda function
# program to sort the list by age with lamda function

people_data = [("Shuvam", 23), 
                ("Riju", 24), 
                ("Mousumi", 43), 
                ("Rinku", 47)
              ]


# using lamda function to sort the list
# people_data.sort(key=lamda parameter:statement) --> syntax of lamda function
people_data.sort(key=lambda person: person[1])      # person[1] denotes the index of age of the perosn in the list
print(people_data)