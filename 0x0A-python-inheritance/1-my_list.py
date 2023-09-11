#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new_list = self[:]
        for i in range (len(new_list)):
            if not isinstance(new_list[i], int):
                raise TypeError("Element must be int")
        print(sorted(new_list))

