#!/usr/bin/python3
""" writes texts into a file and return chars written
    creates the file if file name doesn't exist.
"""


def write_file(filename="", text=""):
    """ writes texts into a file and returns char count written. """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
