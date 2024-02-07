#!/usr/bin/python3
"""
Defines a function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Parameters:
    - my_obj (object): The object to be serialized to JSON.

    Returns:
    - str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
