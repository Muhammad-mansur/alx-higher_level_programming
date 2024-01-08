#!/usr/bin/python3


""" Rectangle Class """


class Rectangle:
    """
    Rectangle

    Args:
        width: private instance
        height: private instance
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves the attribute """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value: new width

        Raises:
            TypeError: if 'value' is not an int
            ValueError: if 'value' is not greater than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ to retrieve the attribute """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value = new height

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0

        return self.width * 2 + self.height * 2

    def __str__(self):
        """ sets the print behaviour of the rectangle object """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for _ in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """ returns a string representation """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message when an instance of rectangle is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        Args:
            rect_1: Rectangle instance 1
            rect_2: Rectangle instance 2

        Raises:
            TypeError: if 'rect_1' is not an instance of Rectangle
            TypeError: if 'rect_2' is not an instance of Rectangle

        Returns:
            rect_1: if both have the same area value
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new rectangle instance using classmethod """
        width = size
        height = size
        return cls(width, height)




