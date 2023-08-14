#!/usr/bin/python3
def no_c(my_string):
    cpy = my_string
    for counter in range (0, len(my_string)):
        if(my_string[counter] == 'c' or my_string[counter] == 'C'):
           del my_string[counter] 
        return (my_string)
