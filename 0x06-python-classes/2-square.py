#!/usr/bin/python3

""" A class square that defines a square """


class Square:
    """
    a class square with private instace attribute and checks for datatype
    """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
