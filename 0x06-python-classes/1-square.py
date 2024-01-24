#!/usr/bin/python3
"""A module for square"""

class Square:
    """Defines a square with a private attribute size."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private and is named '__size'.
        """
        self.__size = size
