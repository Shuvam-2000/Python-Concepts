# dictionaires in python
dict = {
    'name': 'Shuvam Saha',
    "age": 24,
    "desire": "Mousumi",
    "ageOfDesire": 44,
    "smell": "best",
    "taste": "tasty"
}

print(type(dict))

print((dict['desire']))

# chnaging data in the dictionary
dict['name'] = 'Riju Saha'

# adding a new data
dict['city'] = 'Durgapur'

print(dict)

if 'size' in dict:
    print(dict['size'])
elif 'taste' in dict and 'smell' in dict:
    print(dict['taste'],  dict['smell'])
else:
    print('Size matter nahi karta khoobsurart hai bas or apun ko pasand hai')
