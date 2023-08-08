#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if chr(char) != 'e' and chr(char) != 'q':
        print("{}".format(chr(char)), end="")
