"""
This module provides functionality for authenticating teachers.
"""

from file_operations import read_json
from exceptions import AuthenticationError

def authenticate_teacher(teachers_file, name, teacher_id):
    """
    Authenticates a teacher based on name and ID.

    Args:
        teachers_file (str): The file path to the JSON file containing teachers' data.
        name (str): The name of the teacher.
        teacher_id (str): The ID of the teacher.

    Returns:
        bool: True if authentication is successful, otherwise raises an AuthenticationError.

    Raises:
        AuthenticationError: If the teacher's credentials are invalid.
    """
    data = read_json(teachers_file)
    for entry in data:
        if entry['name'] == name and entry['id'] == teacher_id:
            print("Verified Successfully!!!")
            return True
    raise AuthenticationError("Invalid teacher credentials")
