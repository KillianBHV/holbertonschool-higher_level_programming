#!/usr/bin/python3
"""Create a square"""


class Square:
    """Defining the attributes and methods of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Init a new square

        Args:
            size (int) : size of the new square
            position (int, int) : tuple for coordinates
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Return the current coordinates"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position of the square"""
        if (
            not type(value) is int or
            not len(value) == 2 or
            not all(type(num) is int for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' character"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(self.__position[0] * " " + self.__size * "#")
