#!/usr/bin/python3
def no_c(my_string):
    for counter in range (0, len(my_string)):
        cpy[counter] = my_string[counter]
        if(my_string[counter] == 'c' or my_string[counter] == 'C'):
            cpy[counter] = ""
        return (cpy)
