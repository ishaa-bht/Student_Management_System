"""
This module defines the Teacher class for managing teacher information.
"""

import re
from file_operations import append_json, read_json, write_json
from exceptions import NoMatchingNameError

class Teacher:
    """
    A class to represent a teacher.
    """

    def __init__(self, name, subject, teacher_id, address, email, phone_number):
        """
        Initialize a Teacher object.

        Args:
            name (str): The name of the teacher.
            subject (str): The subject taught by the teacher.
            teacher_id (str): The ID of the teacher.
            address (str): The address of the teacher.
            email (str): The email of the teacher.
            phone_number (int): The phone number of the teacher.
        """
        self.name = name
        self.subject = subject
        self.teacher_id = teacher_id
        self.address = address
        self.email = self.validate_email(email)
        self.phone_number = self.validate_phone_number(phone_number)

    def validate_email(self, email):
        """
        Validate the email address.

        Args:
            email (str): The email address to validate.

        Returns:
            str: The validated email address.

        Raises:
            ValueError: If the email address is invalid.
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        raise ValueError("Invalid email address")

    def validate_phone_number(self, phone_number):
        """
        Validate the phone number.

        Args:
            phone_number (int): The phone number to validate.

        Returns:
            int: The validated phone number.

        Raises:
            ValueError: If the phone number is not an integer or does not have 10 digits.
        """
        if isinstance(phone_number, int) and len(str(phone_number)) == 10:
            return phone_number
        raise ValueError("Phone number must be an integer with 10 digits")

    def accept(self, file_path):
        """
        Accept the teacher's information and save it to the JSON file.

        Args:
            file_path (str): The file path to the JSON file.
        """
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
        """
        Display basic information for all teachers.

        Args:
            file_path (str): The file path to the JSON file.
        """
        data = read_json(file_path)
        for entry in data:
            print(
                f"Name: {entry['name']}, Email: {entry['email']}, "
                f"Phone: {entry['phone_number']}, Subject: {entry['subject']}"
            )

    @staticmethod
    def display_full_details(file_path):
        """
        Display full details for all teachers.

        Args:
            file_path (str): The file path to the JSON file.
        """
        print("\nTeacher Record:")
        data = read_json(file_path)
        for entry in data:
            print(
                f"Name: {entry['name']}, Subject: {entry['subject']}, "
                f"ID: {entry['id']}, Address: {entry['address']}, "
                f"Email: {entry['email']}, Phone: {entry['phone_number']}"
            )

    @staticmethod
    def search(file_path, name):
        """
        Search for a teacher by name.

        Args:
            file_path (str): The file path to the JSON file.
            name (str): The name of the teacher to search for.

        Returns:
            dict: The teacher's information if found.

        Raises:
            NoMatchingNameError: If no matching name is found.
        """
        data = read_json(file_path)
        for entry in data:
            if entry['name'] == name:
                return entry
        raise NoMatchingNameError("No matching name found")

    @staticmethod
    def delete(file_path, name):
        """
        Delete a teacher by name.

        Args:
            file_path (str): The file path to the JSON file.
            name (str): The name of the teacher to delete.
        """
        data = read_json(file_path)
        new_data = [entry for entry in data if entry['name'] != name]
        write_json(file_path, new_data)
