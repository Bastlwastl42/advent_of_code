#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 14:10

@author: Sebastian Lehrack

flipping_tiles.py is a script for advent of code day 24
"""

from math import sqrt
import os
from common import load_input_file

class Vector:
    """a 2dimensional vektor class"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return self.a * other.b + self.b * other.b

    def skalar_mult(self, skalar):
        return Vector(self.a * skalar, self.b * skalar)

    def cross_product(self, other):
        pass

    def __abs__(self):
        return round(sqrt(self.a * self.a + self.b * self.b))

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f'({self.a}, {self.b})'


wurzel_drei_halbe = sqrt(3)*0.5
NORTH_EAST = Vector(wurzel_drei_halbe, wurzel_drei_halbe)
NORT_WEST = Vector(-1*wurzel_drei_halbe, wurzel_drei_halbe)
SOUTH_EAST = Vector(wurzel_drei_halbe, -1*wurzel_drei_halbe)
SOUTH_WEST = Vector(-1*wurzel_drei_halbe, -1*wurzel_drei_halbe)
WEST = Vector(-1, 0)
EAST = Vector(1, 0)

def flipping_tiles_from_line(input_lines):
    pass


if __name__ == "__main__":
    print("Welcome to flipping_tiles.py")
    input_lines = load_input_file(os.getcwd())
    print(flipping_tiles_from_line(input_lines))

