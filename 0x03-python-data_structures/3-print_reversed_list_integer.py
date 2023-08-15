#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        length = my_list[::-1]
        for counter in range(0, len(length)):
            print("{:d}".format(length[counter]))
