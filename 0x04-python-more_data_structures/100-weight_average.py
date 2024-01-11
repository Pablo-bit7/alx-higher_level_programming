#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>).

    Args:
    - my_list (list): List of tuples, each containing a score and its corresponding weight.

    Returns:
    - float: Weighted average of the scores.
    """
    if not my_list:
        return 0

    total_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    if total_weight == 0:
        return 0

    return total_sum / total_weight
