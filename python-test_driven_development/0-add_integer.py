#!/usr/bin/python3
"""Defining an addition function"""


def add_integer(a, b=98):
    """
    Get the sum of two integers a and b

    :param a: int
    :param b: int
    :return: int

    >>> add_integer(3, 97)
    100
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    elif not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
