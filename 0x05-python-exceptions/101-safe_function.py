#!/usr/bin/python3

import sys

def safe_function(fct, *args):

    try:
        result = fct(*args)

    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None

    return result
