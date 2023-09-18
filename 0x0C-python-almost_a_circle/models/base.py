#!/usr/bin/python3
""" Base class for future classes in this project. """
import json
import csv
import turtle
import os
from models.to_json_string import to_json_string


class Base:
    """ Base class extra word. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalizaing of the base class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns json string. """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json repr to a file. """
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is None:
            with open("Rectangle.json", 'w') as file:
                file.write('[]')
            with open("Square.json", 'w') as file:
                file.write('[]')
            return 0
        rects = []
        squares = []
        for i in range(len(list_objs)):
            if type(list_objs[i]) is Rectangle:
                rects.append(list_objs[i])
            elif type(list_objs[i]) is Square:
                squares.append(list_objs[i])

        for x in range(len(rects)):
            rects[x] = rects[x].to_dictionary()
        for y in range(len(squares)):
            squares[y] = squares[y].to_dictionary()

        filename = "Rectangle.json"
        with open(filename, 'w') as file:
            file.write(to_json_string(rects))

        filename = "Square.json"
        with open(filename, 'w') as file:
            file.write(to_json_string(squares))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of dictionaries represented by json_string. """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with it's attrs already set. """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            dummy = Rectangle(1, 1)
        if cls == Square:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns instances from file. """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename) as file:
            dicts = Base.from_json_string(file.read())

        objects = [cls.create(**d) for d in dicts]
        return objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves json repr to a file. """
        from models.rectangle import Rectangle
        from models.square import Square

        rects = []
        squares = []
        for i in range(len(list_objs)):
            if type(list_objs[i]) is Rectangle:
                rects.append(list_objs[i])
            elif type(list_objs[i]) is Square:
                squares.append(list_objs[i])

        for x in range(len(rects)):
            rects[x] = rects[x].to_dictionary()
        for y in range(len(squares)):
            squares[y] = squares[y].to_dictionary()

        filename = "Rectangle.csv"
        with open(filename, 'w', newline='') as file:
            outWriter = csv.writer(file)
            for item in rects:
                outWriter.writerow(item.values())

        filename = "Square.csv"
        with open(filename, 'w', newline='') as file:
            outWriter = csv.writer(file)
            for item in squares:
                outWriter.writerow(item.values())

    @classmethod
    def load_from_file_csv(cls):
        """ Returns instances from file. """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            filename = "Rectangle.csv"
        elif cls == Square:
            filename = "Square.csv"

        dicts = []
        with open(filename) as file:
            reader = csv.reader(file)
            if cls == Rectangle:
                for row in reader:
                    data_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }
                    dicts.append(data_dict)
            elif cls == Square:
                for row in reader:
                    data_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                    dicts.append(data_dict)

        for i in range(len(dicts)):
            dicts[i] = cls.create(**dicts[i])

        return dicts

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-250, 250)
        turtle.pendown()

        for rectangle in list_rectangles:
            turtle.color("blue")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.color("red")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()

        turtle.exitonclick()
