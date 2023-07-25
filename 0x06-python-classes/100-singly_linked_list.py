#!/usr/bin/python3
"""Node class to represent a Node"""

class Node():
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (Type(value) is not int):
            print("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            print("next_node must be a Node object")
        else:
            self.__next_node = value
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

class SinglyLinkedList():
    """SinglyLinkedList class to represent a Singly linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
