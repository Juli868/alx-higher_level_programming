#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = 0
    numbers = [0]
    for counter_1 in range(0, len(my_list)):
        for counter_2 in range(len(numbers)):
            if(my_list[counter_1] != numbers[counter_2]):
                numbers.append(my_list[counter_1])
            else:
                continue
    for counter in range(len(numbers)):
        added += numbers[counter]
    return (added)
