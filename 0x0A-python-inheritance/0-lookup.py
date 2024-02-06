#!/usr/bin/python3
""" Defines a function to retrieve attributes and methods of an object. """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj (object): The object for which to retrieve attributes and methods.

    Returns:
    - list: A list containing the attributes and methods of the object.
    """
    return dir(obj)
