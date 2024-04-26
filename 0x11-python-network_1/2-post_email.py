#!/usr/bin/python3

""" Post an email """

import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':

    url = sys.argv[1]

    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')

        print(body)
