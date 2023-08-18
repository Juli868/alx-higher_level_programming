#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = my_list[0]
    for counter in range(len(my_list)):
        if (my_list[counter] > maximum):
            maximum = my_list[counter]
    return (maximum)
