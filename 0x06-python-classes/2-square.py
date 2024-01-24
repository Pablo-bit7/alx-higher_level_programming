#!/usr/bin/python3
"""A module for square"""

class Square:
    """Defines a square with a private attribute size."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
