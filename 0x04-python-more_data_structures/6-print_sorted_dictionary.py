#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    [print("{}: {}".format(i, my_dict[i])) for i in sorted(my_dict)]
