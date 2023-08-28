#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    i = 0
    x += 1
    try:
        while (my_list[x]):
            if (x > i):
                print(my_list[i], end='')
                counter += 1
                x += 1
                i += 1
    except IndexError:
        print("")
    i = 0
    return (counter)
