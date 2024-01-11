#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
    - a_dictionary (dict): Input dictionary.

    Note:
    - Keys are sorted alphabetically.
    - Only keys of the first level are sorted.
    - Values can have any type.
    """
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
