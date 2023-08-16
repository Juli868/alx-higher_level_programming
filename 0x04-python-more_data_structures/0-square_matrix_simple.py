#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for counter in range(len(matrix)):
        new[counter] = list(map(lambda x: x ** 2, matrix[counter]))
    return (new)
