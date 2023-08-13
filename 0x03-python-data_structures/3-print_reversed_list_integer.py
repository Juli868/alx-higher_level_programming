#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = int((len(my_list) - 1) / -1)
    for length in range(0, len(my_list)) :
        print("{:d}".format(my_list[length])) 
