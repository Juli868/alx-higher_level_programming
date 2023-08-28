#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length_1 = len(matrix)
    for counter_1 in range(length_1):
        new = matrix[counter_1]
        print(new, end = ",")
        print("")
