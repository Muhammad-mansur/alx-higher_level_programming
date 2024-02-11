#!/usr/bin/python3

""" class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Calling the super class and
        Assigning the value of size to width and height
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overloading """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size)

    @property
    def size(self):
        """ """
        return self.width

    @size.setter
    def size(self, size):
        """ """
        self.width = size
        self.height = size
