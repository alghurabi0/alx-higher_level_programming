#!/usr/bin/python3
""" make a request id print body only of code < 400 """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(str(sys.argv[1]))
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
