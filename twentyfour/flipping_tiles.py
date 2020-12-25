#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 14:10

@author: Sebastian Lehrack

flipping_tiles.py is a script for advent of code day 24
"""

import os
from math import sqrt, acos, pi, degrees, cos, sin, radians

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

    def dot_product(self, other):
        return self.a * other.a + self.b * other.b

    def __abs__(self):
        return sqrt(self.a * self.a + self.b * self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f'({self.a}, {self.b})'

    def angle(self, other):
        if abs(other) == 0 or abs(self) == 0:
            return 0
        if self.b < other.b:
            sign = -1
        else:
            sign = 1
        return round(acos((self.dot_product(other)) / round((abs(self) * abs(other)), 5)), 5)

    def direction(self):
        if self.b == 0:
            if self.a >= 0:
                return 0
            if self.a < 0:
                return pi
        if self.b < 0:
            return 2 * pi - round((acos(self.a / abs(self))), 5)
        return round((acos(self.a / abs(self))), 5)


wurzel_drei_halbe = sqrt(3) * 0.5
NORTH_EAST = Vector(0.5, wurzel_drei_halbe)
NORTH_WEST = Vector(-0.5, wurzel_drei_halbe)
SOUTH_EAST = Vector(0.5, -1 * wurzel_drei_halbe)
SOUTH_WEST = Vector(-0.5, -1 * wurzel_drei_halbe)
WEST = Vector(-1, 0)
EAST = Vector(1, 0)


def get_tile_pos(line):
    line_iter = iter(line)
    value = next(line_iter, 0)
    tile_position = Vector(0, 0)
    while value != 0:
        if value == 'e':
            tile_position += EAST
        elif value == 'w':
            tile_position += WEST
        elif value == 'n':
            value = next(line_iter)
            if value == 'e':
                tile_position += NORTH_EAST
            elif value == 'w':
                tile_position += NORTH_WEST
        elif value == 's':
            value = next(line_iter)
            if value == 'e':
                tile_position += SOUTH_EAST
            elif value == 'w':
                tile_position += SOUTH_WEST
        value = next(line_iter, 0)
    return round(degrees(tile_position.direction()), 3), round(abs(tile_position), 5)


def flipping_tiles_from_line(input_lines):
    tile_dict = {}
    for line in input_lines:
        # the tile position is a tuple of angle and length
        tile_direction, tile_magnitude = get_tile_pos(line)
        # prepare directions for 360deg symmetry
        # direction is mod pi and negative for values larger 180

        tile_position = (tile_direction, tile_magnitude)
        tile_dict[tile_position] = (tile_dict.get(tile_position, 0) + 1) % 2
    return sum(tile_dict.values())


def get_neightbors(tile, tile_pos):
    # from given tuple of direction and magnitude, reconstruct tile vector
    tile_vector = Vector(tile[1] * cos(radians(tile[0])), tile[1] * sin(radians(tile[0])))
    return_tile_dict = {}
    for adjecent in [EAST, WEST, NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST]:
        new_tile = tile_vector + adjecent
        new_tile_pos = (new_tile.direction(), abs(new_tile))
        return_tile_dict[new_tile_pos] = tile_pos.get(new_tile_pos, 0)
    return return_tile_dict


if __name__ == "__main__":
    print("Welcome to flipping_tiles.py")
    input_lines = load_input_file(os.getcwd())
    print(flipping_tiles_from_line(input_lines))
