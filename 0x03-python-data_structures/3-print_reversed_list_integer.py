#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = -1 * (len(my_list) - 1)
    for counter in range(length, 1):
        print("{:d}".format(my_list[counter]))
