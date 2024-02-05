#!/usr/bin/python3

""" A class geometry """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ implementation not done """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

         Raises:
            TypeError: if value not int
            ValueError: if value less than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
