#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    while (my_list[i]):
        if (x > i):
             try:
                 print("{:d}".format(my_list[i]), end='')
                 i+= 1
                 counter += 1
             except(ValueError, TypeError):
                 i += 1 
        else:
            break
    print("")
    return (counter)
