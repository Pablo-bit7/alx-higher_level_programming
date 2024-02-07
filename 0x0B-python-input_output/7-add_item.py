#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and then saves them to a file using JSON representation.
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Parameters:
    - my_obj (object): The object to be serialized to JSON.
    - filename (str): The name of the text file.

    Returns:
    - None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Create an object from a “JSON file”.

    Parameters:
    - filename (str): The name of the JSON file.

    Returns:
    - object: The Python object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


filename = "add_item.json"

try:
    # Load existing list from file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
