#!/usr/bin/python3

""" Task 10 of 'Project 0x06. Python - Classes and Objects """

from math import pi


class MagicClass:
    """ Magic class """
    def __init__(self, radius=0):
        """ Constructor for magic class
        Args:
            radius: radius of a circle
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ area of a circle """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ circumference of a circle """
        return 2 * math.pi * self.__radius
