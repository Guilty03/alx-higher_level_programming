#!/usr/bin/python3

"""
    This module is Task 2 of the project '0x06. Python -
    Classes and Objects which is a continuation of task 1
    and adds validation for the private instance attribute
"""


class Square:
    """ A Square class """
    def __init__(self, size=0):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
