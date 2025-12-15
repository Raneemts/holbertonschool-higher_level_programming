#!/usr/bin/env python3
"""Defines shapes using duck typing."""

import math


class Shape:
    """Base class for shapes."""

    def area(self):
        """Return the area."""
        raise NotImplementedError

    def perimeter(self):
        """Return the perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
