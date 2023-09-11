#!/usr/bin/python3
class MyList(list):
    list_t = super.__init__
    def print_sorted(self):
        new_list = sorted(list_t)
        return (new_list)

