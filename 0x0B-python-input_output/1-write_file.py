#!/usr/bin/python3
"""
Defines a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number
    of characters written.

    Parameters:
    - filename (str): The name of the text file.
    - text (str): The string to be written to the file.

    Returns:
    - int: The number of characters written (excluding newline).
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        characters_written = len(text)
    return characters_written
