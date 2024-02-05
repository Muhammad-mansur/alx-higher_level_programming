#!/usr/bin/python3

""" Rebel Int """


class MyInt(int):
    """ int """
    def __eq__(self, another):
        return int(self) != another

    def __ne__(self, another):
        return int(self) == another
