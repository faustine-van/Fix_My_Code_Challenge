#!/usr/bin/python3
""" Square """


class Square():
    """ Square class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ set """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an int")

    @property
    def height(self):
        """ retrieve """
        return self.__height

    @height.setter
    def height(self, value):
        """ set """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an int")

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
