# chaining comparision operator in python
# example

# program to determine the upper and lower limit of age in gov exam

print("Goverment Exam Eligibilty Check".title());

print();

name = input("Enter your name : ");
age = int(input("Enter your age : "));

print();

# using chaining comaparision operator 
if 18 <= age <= 28:
    print("You are Eligible {}".format(name));
else:
    print("You are not Eligible {}".format(name));

