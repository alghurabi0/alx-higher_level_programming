#!/usr/bin/python3
""" display json resuslts if any """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = str(sys.argv[1])

    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': q})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
