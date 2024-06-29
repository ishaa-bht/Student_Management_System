import re
from file_operations import append_json, read_json, write_json
from exceptions import NoMatchingNameError

class Teacher:
    def __init__(self, name, subject, teacher_id, address, email, phone_number):
        self.name = name
        self.subject = subject
        self.teacher_id = teacher_id
        self.address = address
        self.email = self.validate_email(email)
        self.phone_number = self.validate_phone_number(phone_number)

    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            raise ValueError("Invalid email address")

    def validate_phone_number(self, phone_number):
        if isinstance(phone_number, int) and len(str(phone_number)) == 10:
            return phone_number
        else:
            raise ValueError("Phone number must be an integer with 10 digits")

    def accept(self, file_path):
        new_data = {
            "name": self.name,
            "subject": self.subject,
            "id": self.teacher_id,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number
        }
        append_json(file_path, new_data)
        print("Teacher added successfully!")

    @staticmethod
    def display_all(file_path):
        data = read_json(file_path)
        for entry in data:
            print(f"Name: {entry['name']}, Email: {entry['email']}, Phone: {entry['phone_number']}, Subject: {entry['subject']}")

    @staticmethod
    def display_full_details(file_path):
        print("\nTeacher Record:")
        data = read_json(file_path)
        for entry in data:
            print(f"Name: {entry['name']}, Subject: {entry['subject']}, ID: {entry['id']}, Address: {entry['address']}, Email: {entry['email']}, Phone: {entry['phone_number']}")

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