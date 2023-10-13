#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    first = sentence[0]

    if len(sentence) == "":
        return None
    else:
        return (length, first)
