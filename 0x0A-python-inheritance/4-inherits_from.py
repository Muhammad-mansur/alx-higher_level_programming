#!/usr/bin/python3

"""
module for inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    checks for subclass
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
