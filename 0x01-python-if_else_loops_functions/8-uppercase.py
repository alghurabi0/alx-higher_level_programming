#!/usr/bin/python3
def uppercase(str):
    result = ""

    for char in str:
        if 'a' <= char <= 'z':
            diff = ord('A') - ord('a')
            upper_char = chr(ord(char) + diff)
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)
    print("{}".format(result))
