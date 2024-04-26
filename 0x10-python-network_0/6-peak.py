#!/usr/bin/python3

""" Find a peak """


def find_peak(list_of_integers):
    """ Peak value """
    if not list_of_integers:
        return None
    else:
        return max(list_of_integers)
