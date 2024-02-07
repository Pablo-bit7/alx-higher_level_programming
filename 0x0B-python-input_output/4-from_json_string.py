#!/usr/bin/python3
"""
Defines a function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string.

    Returns:
    - object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
