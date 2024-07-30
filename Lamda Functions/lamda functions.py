# Lamda Functions In Python
# Example - program to understand the use of lamda function(this code is not of 
# lamda function)

people_data = [("Shuvam", 23), 
                ("Riju", 24), 
                ("Mousumi", 43), 
                ("Rinku", 47)
              ]

# soritng the list by age
def sort_age(age):
   # age[i] is the age in the tuple with index 1   
   return age[1]

# the function sort_age is passed to the argument key 
# the reverse argument=True helps in sorting the list according to the age
people_data.sort(key=sort_age, reverse=True)
print(people_data)

