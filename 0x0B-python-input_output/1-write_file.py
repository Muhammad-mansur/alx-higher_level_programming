#!/usr/bin/python3

""" File """


def write_file(filename="", text=""):
    """ Writes a string to a text file """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
        return len(myFile)
