#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0:
        a0 = 0
        a1 = 0
    elif len_a == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if len_b == 0:
        b0 = 0
        b1 = 0
    elif len_b == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    new_tuple = (a0 + b0, a1 + b1)
    return (new_tuple)
