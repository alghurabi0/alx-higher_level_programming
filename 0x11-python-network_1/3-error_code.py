#!/usr/bin/python3
""" fetch alx website using urllib and print the body """
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            decodedBody = body.decode('utf-8')
            print(decodedBody)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
