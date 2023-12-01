#!/usr/bin/python3
""" sends a post requd print decoded body reponse using urllib """
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = str(sys.argv[1])
    email = str(sys.argv[2])
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        decodedBody = body.decode("utf-8")
        print(decodedBody)
