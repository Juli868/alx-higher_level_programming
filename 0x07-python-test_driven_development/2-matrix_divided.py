#!/usr/bin/python3
def matrix_divided(matrix, div):
    res = []
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res.append(matrix[i][j]/ div)
    return (res)
