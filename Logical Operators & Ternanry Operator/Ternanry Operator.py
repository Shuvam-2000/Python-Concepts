# exapmle for ternanry operator

#  program to check if any person is eligible to vote or note

age = int(input("Enter Your age: "));
haveVoterId = (input("Do You have Your VoterID: ").strip().lower() == "Yes");

print();

# ternanry operator
eligibleForVote = "Eligible To Vote" if age >=18 and haveVoterId else "Not Eligible to Vote Now";

print(eligibleForVote);