#!/usr/bin/python3
""" A function that open a files and reads from it. """


def read_file(filename=""):
    """ A function that read a file after openning it. """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
