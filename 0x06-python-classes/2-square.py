#!/usr/bin/python3
""" Class Square with Attribute size"""


class Square():
    """Attribute size in Class Square"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be >= 0")
        elif (size < 0):
            raise ValueError("size must be an integer")
        else:
            self.__size = int(size)
