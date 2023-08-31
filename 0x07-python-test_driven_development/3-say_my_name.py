#!/usr/bin/python3
""" Prints full name """


def say_my_name(first_name, last_name=""):
    """ Prints full name.
    Args:
        first_name: string
        last_name: string, default is an empty string.

    Returns: My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
