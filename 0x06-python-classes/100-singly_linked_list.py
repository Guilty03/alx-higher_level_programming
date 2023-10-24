#!/usr/bin/python3

"""
    Task 7 of Project '0x06. Python - Classes and Objects'
    This module defines a node and a singly linked list class
"""


class Node:
    """
        A singly linked list node
    Attributes:
        data: integer data of the node
        next_node: holds the next node
    """

    def __init__(self, data, next_node=None):
        """ Initializes a new node instance
        Args:
            data: data to assign to the new node
            next_node: reference to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter method for the data private instance
            attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter method for the data private instance
            attribute
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter method for the next_node private instance
            attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter method for the next_node private instance
            attribute
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ a singly linked list data structure """

    def __init__(self):
        """ initializes a singly linked list instance """
        self.__head = None

    def sorted_insert(self, value):
        """ insert a node into the linked list
        Args:
            value: data of the new node
        """
        new_node = Node(value)
        if self.__head is None or value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr = self.__head
        nextn = self.__head.next_node
        while curr and nextn and nextn.data <= value:
            curr = curr.next_node
            nextn = curr.next_node
        new_node.next_node = nextn
        curr.next_node = new_node

    def __str__(self):
        """ prints the singly linked list """
        curr = self.__head
        nodestr = ""
        while curr:
            nodestr += str(curr.data)
            curr = curr.next_node
            if curr is not None:
                nodestr += "\n"
        return nodestr
