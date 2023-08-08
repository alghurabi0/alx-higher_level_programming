#!/usr/bin/python3
def islower(c):
    if c != "" and c != "EOF":
        if 'a' <= c <= 'z':
            return True
        else:
            return False
    else:
        print("Traceback (most recent call last):")
