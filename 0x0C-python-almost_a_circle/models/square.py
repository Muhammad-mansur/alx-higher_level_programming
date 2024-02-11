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
        """ retrieve the attribute """
        return self.width

    @size.setter
    def size(self, size):
        """ attribute setter """
        self.width = size
        self.height = size

    def __update(self, id=None, size=None, x=None, y=None):
        """ private update """
        if id is not None:
            self.id = id

        if size is not None:
            self.size = size

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Square Update """
        if args:
            self.__update(*args)

        if kwargs:
            self.__update(**kwargs)
