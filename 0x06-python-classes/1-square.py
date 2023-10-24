#!/usr/bin/python3

"""
    This module is Task 1 of the project '0x06. Python -
    Classes and Objects which defines a class andi adds a
    private instance attribute
"""


class Square:
    """ A Square class """
    def __init__(self, size):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        self.__size = size
