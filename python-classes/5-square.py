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

    @property
    def size(self):
        """Return the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' character"""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
