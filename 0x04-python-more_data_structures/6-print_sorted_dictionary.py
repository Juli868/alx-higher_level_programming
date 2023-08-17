#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_d = list(a_dictionary.keys())
    keys_d.sort()
    for counter in range(len(keys_d)):
        print(f"{keys_d[counter]}: {a_dictionary.get(keys_d[counter])}")
