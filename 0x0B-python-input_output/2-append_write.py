#!/usr/bin/python3

""" Text """


def append_write(filename="", text=""):
    """ Appends a string at the end pf a text file """
    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
        return len(myFile)
