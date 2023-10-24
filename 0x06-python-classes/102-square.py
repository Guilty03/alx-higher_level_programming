#!/usr/bin/python3

"""
    This module is Task 9 of the project '0x06. Python -
    Classes and Objects which is a continuation of task 4
    and adds comparators
"""


class Square:
    """ A Square class """
    def __init__(self, size=0):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        self.__size = size

    def area(self):
        """ compute the area of a square
        Return:
            the area
        """
        return self.__size ** 2

    @property
    def size(self):
        """ getter method for the __size private instance
            attribute

        Return:
            __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for the __size private instance
            attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """ evaluate if two squares are equal """
        return self.__size == other.__size

    def __lt__(self, other):
        """ evaluate if a square is less than another """
        return self.__size < other.__size

    def __gt__(self, other):
        """ evaluate if a square is greater than another """
        return self.__size > other.__size

    def __ne__(self, other):
        """ evaluate if a square is different from another """
        return not(self == other)

    def __ge__(self, other):
        """ evaluate if a square is greater than or equal to another """
        return (self == other) or (self > other)

    def __le__(self, other):
        """ evaluate if a square is less than or equal to another """
        return (self == other) or (self < other)
