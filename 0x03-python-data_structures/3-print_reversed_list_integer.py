#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lengh = len(my_list) - 1
    for i in range(lengh, -1, -1):
        print("{:d}".format(my_list[i]))
