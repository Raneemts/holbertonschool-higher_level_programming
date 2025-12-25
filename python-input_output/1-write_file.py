#!/usr/bin/python3
"""Module that contains a function to write text to a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
