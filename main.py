from file_operations import read_json, write_json, append_json
from authentication import authenticate_teacher
from models.teacher import Teacher
from models.student import Student
from exceptions import AuthenticationError, NoMatchingNameError
import json

def add_new_teacher_from_user(file_path):
    try:
        name = input("Enter teacher's name: ")
        subject = input("Enter subject: ")
        teacher_id = input("Enter teacher ID: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")

        teachers = read_json(file_path)
        if any(teacher['teacher_id'] == teacher_id for teacher in teachers):
            raise ValueError("Teacher ID must be unique.")

        new_teacher = Teacher(name, subject, teacher_id, address, email, int(phone_number))
        new_teacher.accept(file_path)
    except ValueError as e:
        print(e)

def add_new_student_from_user(students_file, teachers_file):
    try:
        print("You need to verify yourself as a teacher to add new entries.")
        teacher_name = input("Enter your name: ")
        teacher_id = input("Enter your Id number: ")
        if not authenticate_teacher(teachers_file, teacher_name, teacher_id):
            raise AuthenticationError("Authentication failed. Only teachers can add new data.")

        name = input("Enter student's name: ")
        roll_number = input("Enter roll number: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        marks_input = input('Enter marks (e.g., {"c": 56, "c++": 52, "python": 89}): ')
        marks = json.loads(marks_input)
        address = input("Enter address: ")

        students = read_json(students_file)
        if any(student['roll_number'] == roll_number for student in students):
            raise ValueError("Student roll number must be unique.")

        new_student = Student(name, roll_number, email, int(phone_number), marks, address)
        new_student.accept(students_file, teachers_file)
    except (ValueError,AuthenticationError) as e:
        print(e)

def display_general_info(teachers_file, students_file):
    print("\nTeachers:")
    Teacher.display_all(teachers_file)
    print("\nStudents:")
    Student.display_all(students_file)

def search_record(teachers_file, students_file, name):
    found = False
    try:
        teacher_record = Teacher.search(teachers_file, name)
        print("\nTeacher Record:")
        print(f"Name: {teacher_record['name']}, Subject: {teacher_record['subject']}, ID: {teacher_record['id']}, Address: {teacher_record['address']}, Email: {teacher_record['email']}, Phone: {teacher_record['phone_number']}")
        found = True
    except NoMatchingNameError:
        pass

    try:
        student_record = Student.search(students_file, name)
        print("\nStudent Record:")
        print(f"Name: {student_record['name']}, Roll Number: {student_record['roll_number']}, Email: {student_record['email']}, Phone: {student_record['phone_number']}, Marks: {student_record['marks']}, Address: {student_record['address']}")
        found = True
    except NoMatchingNameError:
        pass

    if not found:
        print("No matching record found.")

def delete_record(teachers_file, students_file, name):
    teacher_deleted = False
    student_deleted = False

    try:
        Teacher.delete(teachers_file, name)
        teacher_deleted = True
    except NoMatchingNameError:
        pass

    try:
        Student.delete(students_file, name)
        student_deleted = True
    except NoMatchingNameError:
        pass

    if teacher_deleted or student_deleted:
        print(f"Record for {name} deleted successfully.")
    else:
        print("No matching name found.")

def determine_pass_fail(students_file):
    pass_students = Student.pass_fail_determination(students_file)
    print("Pass Students:")
    for student in pass_students:
        print(f"Name: {student['name']}, Marks: {student['marks']}")

def find_highest_and_lowest_scores(students_file):
    highest, lowest = Student.highest_and_lowest_scores(students_file)
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

def calculate_percentages(students_file):
    percentages = Student.calculate_percentage_for_all(students_file)
    for name, percentage in percentages:
        print(f"Name: {name}, Percentage: {percentage}")

def calculate_rank(students_file):
    ranks = Student.calculate_rank(students_file)
    for name, rank in ranks:
        print(f"Name: {name}, Rank: {rank}")

# Main Menu
teachers_file = './data/teachers.json'
students_file = './data/students.json'

while True:
    print("\nWelcome to Student and Teacher Management System")
    print("1. Add a new teacher")
    print("2. Add a new student")
    print("3. Display general information")
    print("4. Display full details of all teachers")
    print("5. Display full details of all students")
    print("6. Search for a record")
    print("7. Delete a record")
    print("8. Determine pass/fail")
    print("9. Find highest and lowest scores")
    print("10. Calculate percentages")
    print("11. Calculate rank")
    print("12. Exit")

    choice = input("Enter your choice (1-12): ")

    if choice == '1':
        add_new_teacher_from_user(teachers_file)
    elif choice == '2':
        add_new_student_from_user(students_file, teachers_file)
    elif choice == '3':
        display_general_info(teachers_file, students_file)
    elif choice == '4':
        Teacher.display_full_details(teachers_file)
    elif choice == '5':
        Student.display_full_details(students_file)
    elif choice == '6':
        name = input("Enter name to search: ")
        search_record(teachers_file, students_file, name)
    elif choice == '7':
        name = input("Enter name to delete: ")
        delete_record(teachers_file, students_file, name)
    elif choice == '8':
        determine_pass_fail(students_file)
    elif choice == '9':
        find_highest_and_lowest_scores(students_file)
    elif choice == '10':
        calculate_percentages(students_file)
    elif choice == '11':
        calculate_rank(students_file)
    elif choice == '12':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 12.")

