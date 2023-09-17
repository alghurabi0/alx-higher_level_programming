#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    r3 = Square(5, 2, 2)
    Rectangle.save_to_file_csv([r1, r2, r3])

    with open("Rectangle.csv", "r") as file:
        print(file.read())
    with open("Square.csv", 'r') as file:
        print(file.read())
