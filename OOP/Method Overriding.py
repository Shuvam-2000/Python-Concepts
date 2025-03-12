# method overriding - if same fucntion is made in child class which is already present in
# parent class then the child class one will be exceuted

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
    def __init__(self, fname, lname, age, designation, salary):
        super().__init__(fname, lname, age, designation)
        self.salary = salary
    
    def test_upload(self):
        print("Test Uploaded")

    def leave_application(self):
        super().leave_application()   # super method for calling the parent fucntion
        print("Leave Granted")


# student class inherits(School)
class Student(School):
    def __init__(self, fname, lname, age, designation, role):
        super().__init__(fname, lname, age, designation)
        self.role = role
    def test_answer__upload(self):
        print("Answer Uploaded")


# clerk class inherits(School)
class Clerk(School):
    def upload_official_data(self):
        print("Data Uploaded")


# Teacher Object
Teacher_One = Teacher("Shuvam", "Saha", 24, "Teacher", 30000)
print(Teacher_One.first_name, Teacher_One.last_name,
      Teacher_One.age, Teacher_One.designation, Teacher_One.salary)

Teacher_One.take_attendance()
Teacher_One.leave_application()

print("--------------------------------")

# Student Object
Student_One = Student("Riju", "Saha", 23, "Student", 2)
print(Student_One.first_name, Student_One.last_name,
      Student_One.age, Student_One.designation, Student_One.role)

Student_One.take_attendance()