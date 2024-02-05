#!/usr/bin/python3

""" Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry class """
    def __init__(self, width, height):
        """ constructor """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Area implementation """
        return self.__width * self.__height

    def __str__(self):
        """
        return string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
