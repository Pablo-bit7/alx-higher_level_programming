#!/usr/bin/python3
"""A module for square"""

class Square:
    """Defines a square with private attributes size."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the square area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison based on the square area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison based on the square area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal to comparison based on the square area."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparison based on the square area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal to comparison based on the square area."""
        return self.__gt__(other) or self.__eq__(other)
