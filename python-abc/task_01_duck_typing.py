#!/usr/bin/env python3
"""Shapes: ABC + duck typing (no extra imports)."""

from abc import ABC, abstractmethod

PI = 3.141592653589793


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return PI * (self.__radius ** 2)

    def perimeter(self):
        return 2 * PI * self.__radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
