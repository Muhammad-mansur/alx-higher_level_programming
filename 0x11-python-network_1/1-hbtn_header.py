#!/usr/bin/python3

""" Response header value """

import sys
import urllib.request


if __name__ == '__main__':

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
