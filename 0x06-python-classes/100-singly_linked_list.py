#!/usr/bin/python3
"""
Node
"""


class Node:
    """
    Initialize
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Singly Linked list
"""


class SinglyLinkedList:
    """
    Initialize
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        n_w = Node(value)
        if self.__head is None:
            n_w.next_node = None
            self.__head = n_w
        elif self.__head.data > value:
            n_w.next_node = self.__head
            self.__head = n_w
        else:
            t_p = self.__head
            while t_p.next_node:
                if value < t_p.next_node.data:
                    break
                t_p = t_p.next_node

            n_w.next_node = t_p.next_node
            t_p.next_node = n_w

    def __str__(self):
        t_p = self.__head
        infi = []
        while t_p:
            infi.append(str(t_p.data))
            t_p = t_p.next_node

        return ("\n".join(infi))
