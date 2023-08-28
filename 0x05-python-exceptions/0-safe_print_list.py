#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    i = 0
    while (x > i):
        try:
            print(my_list[i], end='')
            counter += 1
            i += 1
        except IndexError:
            break
    print("")
    return (counter)
