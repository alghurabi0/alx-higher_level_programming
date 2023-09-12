#!/usr/bin/python3
""" Insert a string after a search string. """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a string after a search string. """
    with open(filename) as file:
        copy = file.readlines()

    with open(filename, 'w') as file:
        for line in copy:
            if search_string in line:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
