#!/usr/bin/python3
""" Defines the Base class. """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of a list of dictionaries.

        Parameters:
        - list_dictionaries (list): A list of dictionaries.

        Returns:
        - str: The JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

        Parameters:
        - list_objs (list): A list of instances that inherit from Base.

        Returns:
        - None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
