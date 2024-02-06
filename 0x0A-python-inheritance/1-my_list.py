#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class.

    Public instance method:
    - def print_sorted(self): Prints the list, but sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
