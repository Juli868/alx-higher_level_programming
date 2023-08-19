#!usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length_1 = len(matrix)
    for counter_1 in range(length_1):
        new = matrix[counter_1]
        for counter_2 in range(len(new)):
            print(new[counter_2],end = ' ')
        print("")
