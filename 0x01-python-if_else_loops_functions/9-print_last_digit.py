#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if number < 0:
        n = -number
    n = n % 10
    if number > 0:
        print("{}".format(n), end="")
        return n
    else:
        print("{}".format(n), end="")
        return n
