#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a specified number using map.

    Args:
    - my_list (list): Input list of integers.
    - number (int): Number to multiply each value in the list.

    Returns:
    - list: New list with each value multiplied by the specified number.
    """
    return list(map((lambda i: i * number), my_list))

