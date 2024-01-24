#!/usr/bin/python3
"""A module for MagicClass"""

import math

class MagicClass:
    """A class that represents magical calculations."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance.

        Args:
            radius (int or float): The radius of the magic circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the magic circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the magic circle."""
        return 2 * math.pi * self.__radius
