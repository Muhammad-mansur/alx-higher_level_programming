#!/usr/bin/python3

"""
prints a square
"""


def print_square(size):
    """
    prints a square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
