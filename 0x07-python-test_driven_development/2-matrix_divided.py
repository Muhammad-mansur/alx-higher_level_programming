#!/usr/bin/python3

"""
"""


def matrix_divided(matrix, div):
    """ """
    if type(matrix) is not int and type(matrix[list]) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix / 2
    return new_matrix
