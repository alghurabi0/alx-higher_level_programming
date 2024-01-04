#!/usr/bin/python3
""" make a resquest using requests library"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(str(sys.argv[1]))
    print(r.headers.get("X-Request-Id"))
