#!/usr/bin/python3

"""
A function that reads a text file
"""


def read_file(filename=""):
    """ reads a file and prints to stdout """
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        print(f.read(), end="")
