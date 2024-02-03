#!/usr/bin/python3
""" Defines a function to divide all elements of a matrix. """

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The number by which all elements should be divided.

    Returns:
    list of lists: The resulting matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats.
    - TypeError: If each row of the matrix does not have the same size.
    - TypeError: If div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
