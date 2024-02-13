#!/usr/bin/python3
""" Defines the Rectangle class, a subclass of Base. """
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle.
        - y (int): The y-coordinate of the rectangle.
        - id (int): The identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute. """
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute. """
        self.__height = value

    @property
    def x(self):
        """ Getter for the x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute. """
        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute. """
        self.__y = value
