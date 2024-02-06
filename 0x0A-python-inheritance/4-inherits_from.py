#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a class
that inherited (directly or indirectly) from a specified class."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare with.

    Returns:
    - bool: True if obj is an instance of a class that inherits from a_class;
      False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
