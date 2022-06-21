#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size

    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)


    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)