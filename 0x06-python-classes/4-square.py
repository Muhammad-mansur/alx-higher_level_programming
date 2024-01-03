#!/usr/bin/python3

"""
Square class
"""


class Square:
    """ Square class using setter and getter """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ to set it """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """
        return self.__size ** 2
