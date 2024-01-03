#!/usr/bin/python3

""" Square Class """


class Square:
    """
    square class with a private instance attribute, two public instance
    method that prints to stdout
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ to set it """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints the # character in stdout """
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print("#" * self.__size)
