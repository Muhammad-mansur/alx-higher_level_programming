#!/usr/bin/python3

""" bytecode """

import math


class MagicClass:
    """
    Replicates the behaviour described in the provided bytecode
    """
    def __init__(self, radius):
        """
        Constructor for MagicClass, initializes the instance with given radius

        Args:
            radius: a number representing the radius of the circle

        Raises:
            TypeError: if radius is not a number
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle

        Returns:
            The calculated area of the circle
        """
        return 2 ** self.__radius * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle

        Returns:
            The calculated circumference of the circle
        """
        return 2 * math.pi * self.__radius
