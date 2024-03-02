#!/usr/bin/env python3


""" Search and replace """


def search_replace(my_list, search, replace):
    """
    A function that replaces all occurences of an element
    by another in a new list.

    Args:
        my_list: is the initial list
        search: is the element to replace in the list
        replace: is the new element
    """
    new_list = []

    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
