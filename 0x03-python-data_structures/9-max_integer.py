#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == 0:
        return (0, None)

    highest = my_list[0]

    for i in my_list:
        if i > highest:
            return i
