#!/usr/bin/python3

""" Error code #0 """

import sys
import urllib.request
import urllib.error


if __name__ == '__main__':

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
