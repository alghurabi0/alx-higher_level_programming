#!/usr/bin/python3
""" github id by get requst """
import requests
import sys


if __name__ == "__main__":
    username = str(sys.argv[1])
    token = str(sys.argv[2])
    url = f"https://api.github.com/users/{username}"
    headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {token}',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    r = requests.get(url, headers=headers)
    res = r.json()
    print(res.get("id"))
