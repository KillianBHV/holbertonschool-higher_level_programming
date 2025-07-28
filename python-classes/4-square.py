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

    """This is a setter for the private attribute __size"""
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif if value < 0:
            raise ValueError("size must be >= 0")
        else:
            return self.__size

    """Get the area of a square"""
    def area(self):
        return self.__size * self.__size
