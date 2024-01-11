#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
    - my_list (list): Initial list.
    - search: Element to replace in the list.
    - replace: New element.

    Returns:
    - list: New list with replacements.
    """
    new_list = [replace if elem == search else elem for elem in my_list]
    return new_list

