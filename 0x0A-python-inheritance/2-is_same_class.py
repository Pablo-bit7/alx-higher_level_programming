#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly instance of specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare with.

    Returns:
    - bool: True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
