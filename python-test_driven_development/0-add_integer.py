#!/usr/bin/python3
"""
module that adds two integers
"""


def add_integer(a, b=98):
    """
    adds two integers, if either are floats they are converted
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
