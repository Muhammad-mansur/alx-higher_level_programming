#!/usr/bin/python3

""" A function """


def is_same_class(obj, a_class):
    """
    Returns:
        True: if the object is exactly an intance of the specified class
        False: Otherwise
    """
    if type(obj) is a_class:
        return True

    else:
        return False
