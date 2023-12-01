#!/usr/bin/python3
""" mae a post request using requests"""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(str(sys.argv[1]), data={'email': str(sys.argv[2])})
    print(r.text)
