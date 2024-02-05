#!/usr/bin/python3


""" Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class square that inheritis from Rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return super().area()

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
