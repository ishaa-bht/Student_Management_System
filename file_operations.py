import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_json(file_path, new_data):
    data = read_json(file_path)
    data.append(new_data)
    write_json(file_path, data)
