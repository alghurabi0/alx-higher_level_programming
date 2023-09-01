#!/usr/bin/python3
""" Just a module for text indentation for strings. """


def text_indentation(text):
    """ a function that prints two lines after ? . and :.

    Args:
        text: a string

    Returns: print statements
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    marks = [".", ":", "?"]

    if text == "":
        return print()

    for i, char in enumerate(text):
        if i == len(text) - 1:
            print(char, end="")
        elif text[i - 1] in marks and char == " ":
            continue
        elif char in marks:
            print("{}\n\n".format(char), end="")
        else:
            print(char, end="")
