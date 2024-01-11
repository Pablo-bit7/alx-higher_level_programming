#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
    - matrix (list of lists): 2-dimensional array.

    Returns:
    - list of lists: New matrix with each value squared.
    """
    new_matrix = [[val**2 for val in row] for row in matrix]
    return new_matrix
