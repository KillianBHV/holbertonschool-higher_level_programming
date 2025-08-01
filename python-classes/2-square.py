#!/usr/bin/python3
"""Create a square"""


class Square:
    """Defining the attributes of a square"""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
