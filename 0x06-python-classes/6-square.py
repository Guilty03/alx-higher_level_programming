#!/usr/bin/python3

"""
    This module is Task 6 of the project '0x06. Python -
    Classes and Objects' which is a continuation of task 5
    which adds a new private instance attribute and modifies
    the print method
"""


class Square:
    """ A Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter method for the __position private
            instance attribute

        Return:
            __position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """ setter method for the __position private
            instance attribute
        """
        errormsg = "position must be a tuple of two positive integers"
        if (not isinstance(value, tuple)) or len(value) != 2:
            raise TypeError(errormsg)
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(errormsg)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(errormsg)
        self.__position = value

    def my_print(self):
        """ prints a square using the character #
            if size is 0, prints a blank line
            prints the square on the coordinate specified by position by
            using blank space, if position[1] > 0 don't use space
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for k in range(self.__size):
                print("{}{}".format(" "*self.__position[0], "#"*self.__size))
