"""
This module provides functions to read from, write to, and append JSON data to a file.
"""

import json

def read_json(file_path):
    """
    Reads JSON data from a file.

    Args:
        file_path (str): The path to the JSON file to be read.

    Returns:
        list: The JSON data read from the file. Returns an empty list if the file is not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_json(file_path, data):
    """
    Writes JSON data to a file.

    Args:
        file_path (str): The path to the JSON file to be written.
        data (list): The data to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def append_json(file_path, new_data):
    """
    Appends new JSON data to an existing JSON file.

    Args:
        file_path (str): The path to the JSON file to be appended.
        new_data (dict): The new data to append to the file.
    """
    data = read_json(file_path)
    data.append(new_data)
    write_json(file_path, data)
