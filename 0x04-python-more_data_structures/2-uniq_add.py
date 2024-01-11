#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
    - my_list (list): Input list.

    Returns:
    - int: Sum of unique integers.
    """
    unique_integers = set(my_list)
    sum_unique = sum(unique_integers)
    return sum_unique

