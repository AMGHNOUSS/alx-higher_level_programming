#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lengh = len(my_list)
    list_res = []
    for i in range(lengh):
        if my_list[i] % 2 == 0:
            list_res.append(True)
        else:
            list_res.append(False)
    return list_res
