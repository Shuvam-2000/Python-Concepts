# elif (else if) statment in python 
# example

marksOfMaths = int(input("Enter Marks Of Maths : "));
marksOfScience = int(input("Enter Marks Of Science : "));

print();


if (marksOfMaths >= 90 and marksOfScience >= 90):
    print("Grade A")

elif(marksOfMaths >= 75 and marksOfScience >= 75):
    print("Grade B");

elif(marksOfMaths >= 60 and marksOfScience >= 60):
    print("Grade C")

elif(marksOfMaths >= 40 and marksOfScience >=40):
    print("Grade B")

elif(marksOfMaths < 40 and marksOfScience < 40):
    print("Grade F");

else:
    print("Result Not Declared")

