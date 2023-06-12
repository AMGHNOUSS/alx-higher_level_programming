#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif (len(my_list) - 1) < idx:
        return my_list
    else:
        for i in range(len(my_list) - 1):
            if i >= idx:
                my_list[i] = my_list[i + 1]
        del my_list[len(my_list) - 1]
        return my_list
