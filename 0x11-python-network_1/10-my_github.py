#!/usr/bin/python3

""" Github """

import sys
import requests


if __name__ == '__main__':

    url = "http://api.github.com/user"

    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
