#!/usr/bin/python3
""" Square class inherits from rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class inherits from rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of square class. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Formats how print works on square classes. """
        myStr = "[Square] ("
        myStr += str(self.id) + ") "
        myStr += str(self.x) + "/" + str(self.y) + " - "
        myStr += str(self.width)
        return myStr

    @property
    def size(self):
        """ getter of the size attr. """
        return self.width

    @size.setter
    def size(self, value):
        """ setter of the size attr. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates class attributes values. """
        if args and kwargs:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                i += 1
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        elif args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Returns a dict representation of the instance. """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
