#!/usr/bin/python3
""" Defines a module with a function to retrieve the list of attributes and methods of an object. """

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
    - obj (object): The object for which to retrieve attributes and methods.

    Returns:
    - list: A list containing the attributes and methods of the object.
    """
    return dir(obj)
