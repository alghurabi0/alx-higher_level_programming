#!/usr/bin/python3
""" Defines a Node and a SinglyLinkedLists classes. """


class Node:
    """ Node class with data and next_node attributes. """
    def __init__(self, data, next_node=None):
        """ Initialization of the Node instance. """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """ Gets the data attribute of the instance. """
        return self.__data
    
    @data.setter
    def data(self, value):
        """ Sets the data attribute of the instance.
    
        Args:
            value: integer to set for the data.
            """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        """ Returns the next_node value of the Node instance. """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """ Sets the next_node value of the Node instance.
        
        Args:
            value: Node instance to be set as a next_node value.
            """
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
    
class SinglyLinkedList:
    """ Defines a SinglyLinkedList classl. """
    def __init__(self):
        """ Initialization of the SinglyLinkedList instance. """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node to the list.
        Args:
            value: node to be inserted.
            """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def __str__(self):
        """ Format how the list is printed on the screen. """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
            return result