#!/usr/bin/python3

"""
A class MyList that inherits from list
"""


class MyList(list):
    """ prints the list but sorted """
    def print_sorted(self):
        """ Prints sorted list """
        print(sorted(self))
