#!/usr/bin/python3
"""
Defines a function that writes an Object to a text file,
using a JSON representation.
"""
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
