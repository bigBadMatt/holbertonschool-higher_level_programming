#!/usr/bin/python3
"""
Class for a rectangle object
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Object
    """
    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
