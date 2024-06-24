#  string methods 
#  example

text = " My name is Shuvam Saha    ";

# upper method to make the text in the string in uppercase
print(text.upper());

# lower method to make the text in the string in lowercase
print(text.lower());

# title method to make first word of every sentence in uppercase
print(text.title());

# strip method to remove extra spaces from the string
print(text.strip());

# lstrip method to remove space from the left side 
print(text.lstrip());

# lstrip method to remove space from the right side 
print(text.rstrip());

# find method used for giving location of the index of any character
print(text.find("Shuv"));

# replae method used for replacing any item or word from the string
print(text.replace("My", "His"));

# in method for finding any item in the string with true or false
print("name" in text);

# not method for finding any item in the string with true or false
print("your" not in text);
