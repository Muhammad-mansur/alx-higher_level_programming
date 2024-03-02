#!/usr/bin/python3

""" Multiply by 2 """


def multiply_by_2(a_dictionary):
    new_dict = {}

    for key, value in a_dictionary.items():
        new_dict[key] = value * 2

    return new_dict
