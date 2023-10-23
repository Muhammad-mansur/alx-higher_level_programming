#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    rslt = None
    try:
        rlt = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
    return rlt
