#!/usr/bin/python3
def square_matrix_simple(matrix = []):
    new_matrix = []

    for raw in matrix:
        new_raw = []
        for num in raw:
            new_raw.append(num * num)
        new_matrix.append(new_raw)

    return new_matrix
