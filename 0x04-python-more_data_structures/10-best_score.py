#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    list_keys = list(a_dictionary.keys())
    big = a_dictionary[list_keys[0]]
    for i in list_keys:
        if big < a_dictionary[i]:
            big = a_dictionary[i]
            big_key = i
    return big_key
