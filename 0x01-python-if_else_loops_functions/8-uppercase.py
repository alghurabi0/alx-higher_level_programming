#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            diff = ord('A') - ord('a')
            upper_char = chr(ord(char) + diff)
            print("{}".format(upper_char), end="")
        else:
            print("{}".format(char), end="")
    print()
