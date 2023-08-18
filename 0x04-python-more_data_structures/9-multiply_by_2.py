#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys_list = list(a_dictionary.keys())
    cpy = a_dictionary.copy()
    for counter in keys_list:
        cpy[counter] *= 2
    return (cpy)
