#!/usr/bin/python3

def magic_calculation(a, b):
    rlt = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            rlt += (a ** b) / i
        except:
            rlt += b + a
            break

    return rlt
