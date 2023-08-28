#!/usr/bin/python3
def best_score(a_dictionary):
    keys_list = list(a_dictionary.keys())
    cpy = a_dictionary.copy()
    if len(cpy)== 0:
        return None
    maximum = cpy[0]
    for counter in keys_list:
        if(cpy[counter] > maximum):
            maximum = cpy[counter]
    return (maximum)

