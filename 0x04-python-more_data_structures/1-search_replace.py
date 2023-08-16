#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = list(map(lambda num: replace if search == num else num, my_list))
    return (cp)
