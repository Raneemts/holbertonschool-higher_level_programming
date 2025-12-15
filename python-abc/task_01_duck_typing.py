#!/usr/bin/env python3
"""Defines the abstract base class Shape and concrete classes Circle and Rectangle."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class for a circle."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Concrete class for a rectangle."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
