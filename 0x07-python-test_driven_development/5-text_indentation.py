#!/usr/bin/python3
""" Defines a function to print a text with 2 new lines after each of these characters: ., ? and :. """

def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_characters = ['.', '?', ':']
    current_line = ''

    for char in text:
        current_line += char

        if char in end_characters:
            print(current_line.strip())
            print()
            current_line = ''

    if current_line.strip():  # Print the remaining line if it's not empty
        print(current_line.strip())
