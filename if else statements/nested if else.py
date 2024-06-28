# nested if else statement in python
# example

# check the legal age of marriage for male and female in india

print("Legal Age Of Marriage In India".upper());

gender = input("Enter Your Gender Male (M) or Female (F): ");
age = int(input("Enter Your Age: "));

if (age >= 21 and gender == "M".lower()):
    print("You are legally eligible for marriage");

elif(age >= 18 and gender == "F".lower()):
    print("You are legally eligible for marriage");

else:
    print("You are Not Eligible Now"); 