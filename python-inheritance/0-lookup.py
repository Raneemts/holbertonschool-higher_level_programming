#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
