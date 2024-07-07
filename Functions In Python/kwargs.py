# **kwargs in python
# example

# items function is used to return name and 
# value of the arguments in the function

def student_info_add(**school):
    for n , m in school.items():
        print("{} : {}".format(n,m))

student_info_add(name="Shuvam", rollno = 2, age = 23)
