#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
    - set_1 (set): First set.
    - set_2 (set): Second set.

    Returns:
    - set: Set of common elements.
    """
    common_set = set_1.intersection(set_2)
    return common_set
