#!/usr/bin/python3
""" Defines the Base class. """


class Base:
    """ Base class for other classes. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for the Base class.

        Parameters:
        - id (int): Optional, if provided, assigns it to the id attribute.
                    Otherwise, increments __nb_objects and assigns the new
                    value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
