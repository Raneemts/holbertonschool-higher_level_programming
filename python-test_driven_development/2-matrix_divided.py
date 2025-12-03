#!/usr/bin/python3
"""
This module defines the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float)

    Returns:
        A new matrix with each value divided by div and rounded to 2 decimals.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if matrix rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """

    # Validate matrix is a list of lists
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix)
        or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Row length consistency check
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # Validate each element in row
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with divided values
    return [[round(num / div, 2) for num in row] for row in matrix]
