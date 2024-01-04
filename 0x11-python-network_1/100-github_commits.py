#!/usr/bin/python3
""" get github last 10 commeits """
import sys
import requests


if __name__ == "__main__":
    repo = str(sys.argv[1])
    username = str(sys.argv[2])
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    r = requests.get(url, headers=headers)
    res = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                res[i].get("sha"),
                res[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
