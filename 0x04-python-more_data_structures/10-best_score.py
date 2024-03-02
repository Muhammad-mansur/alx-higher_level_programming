#!/usr/bin/python3

""" Best score """


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary, key=a_dictionary.get)

    return max_value
