#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new = []

    for a in range(list_length):
        try:
            m = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            m = 0
        except TypeError:
            print("wrong type")
            m = 0
        except IndexError:
            print("out of range")
            m = 0
        finally:
            new.append(m)

    return new
