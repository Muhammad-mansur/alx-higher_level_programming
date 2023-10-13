#!/usr/bin/python3

def max_integer(my_list=[]):

    length = len(my_list)

    if length == 0:
        return None

    highest = my_list[0]

    for i in my_list:
        if i > highest:
            highest = i

    return highest
