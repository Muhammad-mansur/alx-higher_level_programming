#!/usr/bin/python3

""" A square class """


class Square:
    """
    A square class with two private instance attribute and two public
    instance method
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ to set it """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ to retrieve it """
        return self.__position

    @position.setter
    def position(self, value):
        """ to set it """
        self.__position = value

        if type(value) != tuple or type(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ return the current square area """
        self.__size ** 2

    def my_print(self):
        """ """
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
