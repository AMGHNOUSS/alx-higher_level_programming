#!/usr/bin/python3
def best_score(a_dictionary):
    big = 0
    if a_dictionary == None:
        return None
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        if big < a_dictionary[i]:
            big = a_dictionary[i]
            big_key = i
    return big_key
    
