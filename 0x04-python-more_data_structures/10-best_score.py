#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    list_keys = list(a_dictionary.keys())
    a = list_keys[0]
    big = a_dictionary[a]
    for i in list_keys:
        if big < a_dictionary[i]:
            big = a_dictionary[i]
            big_key = i
    return big_key
