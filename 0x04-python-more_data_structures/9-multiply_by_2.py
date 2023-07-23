#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dictionary = a_dictionary.copy()
    list_keys = list(a_new_dictionary.keys())
    for i in list_keys:
        a_new_dictionary[i] *= 2
    return (a_new_dictionary)
