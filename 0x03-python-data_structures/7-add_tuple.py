#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_t = [0, 0]
    cp_1 = list(tuple_a)
    cp_2 = list(tuple_b)
    while (len(cp_1) != 2):
        cp_1.append(0)
    while (len(cp_2) != 2):
        cp_2.append(0)
    for counter in range(0,2):
            new_t[counter] = cp_1[counter] + cp_2[counter]
    return (new_t)
