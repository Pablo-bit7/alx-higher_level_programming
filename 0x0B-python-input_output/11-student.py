#!/usr/bin/python3
"""
Class Student that defines a student with public instance attributes
and methods to retrieve a dictionary representation and reload attributes.
"""


class Student:
    """
    Represents a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): A list of strings specifying which attributes to
        retrieve.

        Returns:
        - dict: A dictionary containing the specified attributes of the
        Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in the
        provided dictionary.

        Parameters:
        - json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
