#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lengh = len(my_list)
    for i in range(1, lengh + 1):
        print("{:d}".format(my_list[-i]))
