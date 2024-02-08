#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure (list, dictionary, string, integer, and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary with serializable attributes.

    Parameters:
    - obj: An instance of a Class.

    Returns:
    - dict: A dictionary representation of the object
    with serializable attributes.
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return obj.__str__()
