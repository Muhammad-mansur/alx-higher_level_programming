#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    result = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            square_v = matrix[i][j] ** 2
            result[i][j] = square_v

    return result
