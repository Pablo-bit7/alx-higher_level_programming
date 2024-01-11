#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
    - a_dictionary (dict): Input dictionary.
    - key (str): Key to delete (default is an empty string).

    Returns:
    - dict: Updated dictionary after deletion.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
