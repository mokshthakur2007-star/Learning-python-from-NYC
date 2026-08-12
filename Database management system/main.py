import json
from abc import ABC, abstractmethod
from pathlib import Path

# from numpy import save

Database = "School_Database.json" #main database
data = {"students": [], "teachers": []} # copy database
if Path(Database).exists():
    with open(Database, "r") as f:
        content =  f.read()
        if content:
            data = json.loads(content)

def save_data():
    with open(Database, "w") as f:
        json.dump(data, f, indent=4)

class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass
    
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def view_details(self):
        pass
    
    @staticmethod
    def validate_email(email):
        if "@ris.com" in email:
            return True
        return False



class Student(Persons):
    def get_roles(self):
        return "Student"
    
    def register(self):
        name = input("Enter student name: ")
        
        age = int(input("Enter student age: "))
        if age < 5 or age > 18:
            print("Invalid age, student age must be between 5 and 18.")
            return
        
        gender = input("Enter student gender: ")

        student_id = input("Enter student ID: ")
        if any(student["student_id"] == student_id for student in data["students"]):
            print("Student ID already exists.")
            return
        
        email = input("Enter student email: ")
        if not Persons.validate_email(email):
            print("Invalid email format, email must be in format of @ris.com")
            return
        
        
        data["students"].append({
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "student_id": student_id,
            "grades" : {}
        })
        save_data()
        print("Student registered successfully.")
    
    def view_details(self):
        view_id = input("Enter student ID to view details: ")
        for student in data["students"]:
            if student["student_id"] == view_id:
                print(f"Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}, Email: {student['email']}, Grades: {student.get('grades', 'No grades available')}")
                break
        else:
            print("Student not found.")
    
    def add_grades(self):
        student_id = input("Enter student ID to add grades: ")
        for student in data["students"]:
            if student["student_id"] == student_id:
                grades = input("Enter grades (comma separated) (in the order of subjects: Maths, Science, English, Social Science and Sanskrit ): ")
                student["grades"] = [int(grade) for grade in grades.split(",")]
                save_data()
                print("Grades added successfully.")
                break
        else:
            print("Student not found.")
    
    def edit_details(self):
        student_id = input("Enter student ID to edit details: ")
        for student in data["students"]:
            if student["student_id"] == student_id:
                name = input(f"Enter new name (current: {student['name']}): ")
                age = int(input(f"Enter new age (current: {student['age']}): "))
                gender = input(f"Enter new gender (current: {student['gender']}): ")
                email = input(f"Enter new email (current: {student['email']}): ")
                if not Persons.validate_email(email):
                    print("Invalid email format, email must be in format of @ris.com")
                    return
                student["name"] = name
                student["age"] = age
                student["gender"] = gender
                student["email"] = email
                save_data()
                print("Student details updated successfully.")
                break
        else:
            print("Student not found.")
        
    def delete_details(self):
        student_id = input("Enter student ID to delete details: ")
        for i, student in enumerate(data["students"]):
            if student["student_id"] == student_id:
                del data["students"][i]
                save_data()
                print("Student details deleted successfully.")
                break
        else:
            print("Student not found.")
    
    def edit_grades(self):
        student_id = input("Enter student ID to edit grades: ")
        for student in data["students"]:
            if student["student_id"] == student_id:
                grades = input("Enter new grades (comma separated) (in the order of subjects: Maths, Science, English, Social Science and Sanskrit ): ")
                student["grades"] = [int(grade) for grade in grades.split(",")]
                save_data()
                print("Grades updated successfully.")
                break
        else:
            print("Student not found.")


class Teacher(Persons):
    def get_roles(self):
        return "Teacher"

    def register(self):
        name = input("Enter teacher name: ")

        age = int(input("Enter teacher age: "))

        gender = input("Enter teacher gender: ")
        
        subjects = input("Subjects taught by the teacher (comma separated): ")

        teacher_id = input("Enter teacher ID: ")
        if any(teacher["teacher_id"] == teacher_id for teacher in data["teachers"]):
            print("Teacher ID already exists.")
            return
        email = input("Enter teacher email: ")
        if not Persons.validate_email(email):
            print("Invalid email format, email must be in format of @ris.com")
            return
        
        for teacher in data["teachers"]:
            if teacher["teacher_id"] == teacher_id:
                print("Teacher ID already exists.")
                return
        
        data["teachers"].append({
            "name": name,
            "age": age,
            "gender": gender,
            "email": email, 
            "teacher_id": teacher_id,
            "subjects": [subject.strip() for subject in subjects.split(",")]
        })
        save_data()
        print("Teacher registered successfully.")
    
    def view_details(self):
        view_id = input("Enter teacher ID to view details: ")
        for teacher in data["teachers"]:
            if teacher["teacher_id"] == view_id:
                print(f"Name: {teacher['name']}, Age: {teacher['age']}, Gender: {teacher['gender']}, Email: {teacher['email']}")
                break
        else:
            print("Teacher not found.")
    
    def edit_details(self):
        teacher_id = input("Enter teacher ID to edit details: ")
        for teacher in data["teachers"]:
            if teacher["teacher_id"] == teacher_id:
                name = input(f"Enter new name (current: {teacher['name']}): ")
                age = int(input(f"Enter new age (current: {teacher['age']}): "))
                gender = input(f"Enter new gender (current: {teacher['gender']}): ")
                email = input(f"Enter new email (current: {teacher['email']}): ")
                subjects = input(f"Enter new subjects (current: {', '.join(teacher['subjects'])}): ")
                if not Persons.validate_email(email):
                    print("Invalid email format, email must be in format of @ris.com")
                    return
                teacher["name"] = name
                teacher["age"] = age
                teacher["gender"] = gender
                teacher["email"] = email
                teacher["subjects"] = [subject.strip() for subject in subjects.split(",")]
                save_data()
                print("Teacher details updated successfully.")
                break
        else:
            print("Teacher not found.")
    
    def delete_details(self):
        teacher_id = input("Enter teacher ID to delete details: ")
        for i, teacher in enumerate(data["teachers"]):
            if teacher["teacher_id"] == teacher_id:
                del data["teachers"][i]
                save_data()
                print("Teacher details deleted successfully.")
                break
        else:
            print("Teacher not found.")


stud = Student()
teach = Teacher()

print("Welcome to the School Database Management System")
print("Please select an option:")
print("press 0 to exit the program")
print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add student grades")
print("press 4 to view student details")
print("press 5 to view teacher details")
print("press 6 to edit student details")
print("press 7 to edit teacher details")
print("press 8 to delete student details")
print("press 9 to delete teacher details")
print("press 10 to edit grade details")

choice = int(input("Enter your choice : "))

if choice == 0:
    print("Exiting the program.")
    exit()

if choice == 1:
    stud.register()

if choice == 2:
    teach.register()

if choice == 3:
    stud.add_grades()

if choice == 4:
    stud.view_details()

if choice == 5:
    teach.view_details()

if choice == 6:
    stud.edit_details()

if choice == 7:
    teach.edit_details()

if choice == 8:
    stud.delete_details()

if choice == 9:
    teach.delete_details()

if choice == 10:
    stud.edit_grades()