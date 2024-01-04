#!/usr/bin/python3
""" make a request to alx site using urllib and printing header """
import urllib.request
import sys


if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        desiredHeader = "X-Request-Id"
        if desiredHeader in response.headers:
            print(response.headers[desiredHeader])
