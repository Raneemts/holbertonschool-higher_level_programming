#!/usr/bin/python3
"""
This module defines the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix (list): list of lists of integers/floats.
        div (int or float): divisor.

    Returns:
        list: new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
            if rows are not the same size, or if div is not a number.
        ZeroDivisionError: if div is zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
