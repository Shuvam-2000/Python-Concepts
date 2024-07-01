# logical operator in python 
# example

# program to check the eligibilty of admission in college 

print("College Admission Eligibilty Criteria Check");

print();

age = int(input("Enter Your age : "));
percentageClass12 = int(input("Enter Your percentage for Class 12 : "));
percentageClass10 = int(input("Enter Your percentage for Class 10 : "));
criminalCase = bool(input("Any Criminal Backgorund (Yes/No) : "));

print();


if (age < 18):
    print("You are not of the correct age: ");

elif(percentageClass12 >= 60 or percentageClass10 >= 60 
     and not criminalCase):
    print("You are Eligible for Admission");

else:
    print("You are not Eligible for Admission");

