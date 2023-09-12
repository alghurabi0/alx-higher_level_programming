#!/usr/bin/python3
""" Appends text to the end of a file. """


def append_write(filename="", text=""):
    """ Appends text to the end of a file. """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
