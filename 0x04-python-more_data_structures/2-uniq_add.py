#!/usr/bin/python3

""" Unique addition """


def uniq_add(my_list=[]):
    unique_integers = set()

    for num in my_list:
        unique_integers.add(num)

    sum_int = sum(unique_integers)

    return sum_int
