#!/usr/bin/python3
""" Rectangle class subclasses base class. """
from models.base import Base
# Base = __import__('base').Base


class Rectangle(Base):
    """ Rectangle class subclasses base class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization of rectangle class. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the width property. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the width property. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the width. """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ gets the width property. """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the width. """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ gets the width property. """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the width. """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ calculates the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle represented by #. """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ Formats how print work on this class. """
        myStr = "[Rectangle] "
        myStr += "(" + str(self.id) + ")" + " "
        myStr += str(self.__x) + "/" + str(self.__y) + " - "
        myStr += str(self.__width) + "/" + str(self.__height)
        return myStr

    def update(self, *args, **kwargs):
        """ Updates the rectangle attributes. """
        if args and kwargs:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
                i += 1
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
        elif args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """ Returns a dict representation of the instance. """
        myDict = {}
        myDict['x'] = self.__x
        myDict['width'] = self.__width
        myDict['id'] = self.id
        myDict['height'] = self.height
        myDict['y'] = self.__y
        return myDict
