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
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows of the matrix have the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
