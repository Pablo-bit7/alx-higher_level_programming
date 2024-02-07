#!/usr/bin/python3
"""
Defines a function that reads a text file (UTF8) and prints it to stdout.
"""

def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Parameters:
    - filename (str): The name of the text file.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
