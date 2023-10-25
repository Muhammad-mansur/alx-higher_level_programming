#!/usr/bin/python3


class Square:
    """
    The Square class defines a square and provides size-related functionality.
    """

    def __init__(self, size=0):
        """
        Constructor for the Square class

        Args:
            size (int, optional): The size of the square

        Raises:
            TypeError: if 'size' is not an integer
            ValueError: if 'size' is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: the size of the square
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size value

        Raises:
            TypeError: if 'value' is not an integer
            ValueError: if 'value' is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
