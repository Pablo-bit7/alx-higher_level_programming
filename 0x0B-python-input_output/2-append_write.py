#!/usr/bin/python3
"""
Defines a function that appends a string to the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return
    the number of characters added.

    Parameters:
    - filename (str): The name of the text file.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
