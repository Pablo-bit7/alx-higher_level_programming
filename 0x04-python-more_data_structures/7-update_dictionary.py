#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Args:
    - a_dictionary (dict): Input dictionary.
    - key (str): Key to replace or add.
    - value: Value associated with the key.

    Returns:
    - dict: Updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
