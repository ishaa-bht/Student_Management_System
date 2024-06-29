from file_operations import read_json
from exceptions import AuthenticationError

def authenticate_teacher(teachers_file, name, teacher_id):
    data = read_json(teachers_file)
    for entry in data:
        if entry['name'] == name and entry['id'] == teacher_id:
            print("Verified Successfully!!!")
            return True
    raise AuthenticationError("Invalid teacher credentials")
