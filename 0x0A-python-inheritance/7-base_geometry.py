#!/usr/bin/python3

""" A class geometry """


class BaseGeometry:
    """
    Raises:
        Exception: area() is not implemented
        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value < 0 or value == 0:
            raise ValueError("<name> must be greater than 0")
