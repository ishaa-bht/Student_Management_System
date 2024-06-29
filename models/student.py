import re
from file_operations import append_json, read_json, write_json
from authentication import authenticate_teacher
from exceptions import NoMatchingNameError
from exceptions import AuthenticationError

class Student:
    def __init__(self, name, roll_number, email, phone_number, marks, address):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.phone_number = phone_number
        self.marks = marks
        self.address = address

    def accept(self, file_path, teachers_file):
        try:
            new_data = {
                "name": self.name,
                "roll_number": self.roll_number,
                "email": self.email,
                "phone_number": self.phone_number,
                "marks": self.marks,
                "address": self.address
            }
            append_json(file_path, new_data)
            print("Student added successfully!")
        except AuthenticationError as e:
            print(e)

    @staticmethod
    def display_all(file_path):
        data = read_json(file_path)
        for entry in data:
            print(f"Name: {entry['name']}, Email: {entry['email']}, Phone: {entry['phone_number']}, Marks: {entry['marks']}")

    @staticmethod
    def display_full_details(file_path):
        print("\nStudent Record:")
        data = read_json(file_path)
        for entry in data:
            print(f"Name: {entry['name']}, Roll Number: {entry['roll_number']}, Email: {entry['email']}, Phone: {entry['phone_number']}, Marks: {entry['marks']}, Address: {entry['address']}")

    @staticmethod
    def search(file_path, name):
        data = read_json(file_path)
        for entry in data:
            if entry['name'] == name:
                return entry
        raise NoMatchingNameError("No matching name found")

    @staticmethod
    def delete(file_path, name):
        data = read_json(file_path)
        new_data = [entry for entry in data if entry['name'] != name]
        write_json(file_path, new_data)

    @staticmethod
    def pass_fail_determination(file_path):
        data = read_json(file_path)
        pass_students = []
        for entry in data:
            if all(mark >= 32 for mark in entry['marks'].values()):
                pass_students.append({
                    'name': entry['name'],
                    'marks': entry['marks']
                })
        return pass_students

    @staticmethod
    def highest_and_lowest_scores(file_path):
        data = read_json(file_path)
        passed_students = [entry for entry in data if all(mark >= 32 for mark in entry['marks'].values())]
        total_marks = [sum(entry['marks'].values()) for entry in passed_students]
        highest = max(total_marks) if total_marks else "-"
        lowest = min(total_marks) if total_marks else "-"
        return highest, lowest

    @staticmethod
    def calculate_percentage(marks):
        total_marks = sum(marks.values())
        if any(mark < 32 for mark in marks.values()):
            return "-"
        return round((total_marks / (len(marks) * 100)) * 100, 3)

    @staticmethod
    def calculate_percentage_for_all(file_path):
        data = read_json(file_path)
        percentages = []
        for entry in data:
            percentage = Student.calculate_percentage(entry['marks'])
            percentages.append((entry['name'], percentage))
        return percentages

    @staticmethod
    def calculate_rank(file_path):
        data = read_json(file_path)
        passed_students = [entry for entry in data if all(mark >= 32 for mark in entry['marks'].values())]
        sorted_data = sorted(passed_students, key=lambda x: sum(x['marks'].values()), reverse=True)
        ranks = []
        for index, entry in enumerate(sorted_data):
            ranks.append((entry['name'], index + 1))
        return ranks