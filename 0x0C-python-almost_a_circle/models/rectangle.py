#!/usr/bin/python3

""" class rectangle """


from models.base import Base


class Rectangle(Base):
    """ class initialisation """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ retrieves the attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Arg:
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
        """ retrieves the attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Arg:
            value: new height

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def x(self):
        """ retrieves the attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Arg:
            value: new x

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ retrieves the attribute """
        return self.__y

    @y.setter
    def x(self, value):
        """
        Arg:
            value: new y

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def validate(self, value, name):
        """ Validates Attributes """
        if type(value) is not int:
            raise TypeError(name + "must be an integer")

        if self.__width <= 0 and self.__height <= 0:
            raise ValueError(name + "must be > 0")

        if self.__x < 0 and self.__y < 0:
            raise ValueError(name + "must be >= 0")

    def area(self):
        """ returns the area value of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the rectangle instance with the character # """
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ Overriding the medthod """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, 
                self.y, self.width, self.height)
