#!/usr/bin/python3
""" A class inherits from list object and sorts it content(integer). """


class MyList(list):
    """ A class that inherits form list. """

    def print_sorted(self):
        """ Prints the list's content sorted ascending. """
        if len(self) == 0:
            return print([])
        swaps = -1
        while (swaps != 0):
            swaps = 0
            for i in range(len(self) - 1):
                if (self[i] > self[i + 1]):
                    self[i], self[i + 1] = self[i + 1], self[i]
                    swaps = swaps + 1
        print(self)
