#!/usr/bin/python3

"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ 
    divides all elements of a matrix.

        Args:
            matrix: list of lists of integers or floats
            div: a number (integer or float)

        Return: a new matrix with All elements of the matrix
        should be divided by div, rounded to 2 decimal places
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_message)
    for row in matrix:
        if not isintance(row, list):
            raise TypeError(error_message)
        for x in row:
            if not isintance(x, int) and not isinstance(x, float):
                raise TypeError(error_message)

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
