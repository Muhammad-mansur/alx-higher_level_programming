#!/usr/bin/python3

import sys

if __name__ == "__main__":

    argc = len(sys.argv)

    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))