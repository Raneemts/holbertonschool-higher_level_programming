#!/usr/bin/python3
#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
