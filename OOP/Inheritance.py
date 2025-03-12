# inheritance

# school class
class School:
    def __init__(self, fname, lname, age, designation):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.designation = designation

    def take_attendance(self):
        print("Attendace Marked As Present")

    def leave_application(self):
        print("Leave Application Submitted")


# teacher class inherits(School)
class Teacher(School):
    def test_upload(self):
        print("Test Uploaded")


# student class inherits(School)
class Student(School):
    def test_answer__upload(self):
        print("Answer Uploaded")


# clerk class inherits(School)
class Clerk(School):
    def upload_official_data(self):
        print("Data Uploaded")


# Teacher Object
Teacher_One = Teacher("Shuvam", "Saha", 24, "Teacher")
print(Teacher_One.first_name, Teacher_One.last_name, Teacher_One.age, Teacher_One.designation)

Teacher_One.take_attendance()

print("--------------------------------")

# Student Object
Student_One = Student("Riju", "Saha", 23, "Student")
print(Student_One.first_name, Student_One.last_name, Student_One.age, Student_One.designation)

Student_One.take_attendance()
