#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = my_list[::-1]
    for counter in range(0,len(length)):
        print("{:d}".format(length[counter]))
