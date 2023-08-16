#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_t = [0, 0]
    if(len(tuple_a) == 2 and len(tuple_b) == 2):
        for counter in range(0,2):
            new_t[counter] = tuple_a[counter]+ tuple_b[counter]
        return (new_t)
