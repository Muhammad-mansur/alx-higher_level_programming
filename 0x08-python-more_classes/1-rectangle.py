#!/usr/bin/python3

""" A rectangle class """


class Rectangle:
    """ A rectangle class with two private instance attribute """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ to retrieve the attribute """
        return __width

    @width.setter
    def width(self, value):
        """ to set the attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ to retieve the attribute """
        return self._height

    @height.setter
    def height(self, value):
        """ to set the attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
