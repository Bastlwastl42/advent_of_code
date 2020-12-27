#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 14:10

@author: Sebastian Lehrack

flipping_tiles.py is a script for advent of code day 24
"""

import os
from copy import deepcopy
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

FLIP_TO_WHITE_RULE = [0, 3, 4, 5, 6]
FLIP_TO_BLACK_RULE = [2]


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
    return round(degrees(tile_position.direction()), 1), round(abs(tile_position), 1)


def flipping_tiles_from_line(input_lines):
    tile_dict = {}
    for line in input_lines:
        # the tile position is a tuple of angle and length
        tile_direction, tile_magnitude = get_tile_pos(line)
        # prepare directions for 360deg symmetry
        # direction is mod pi and negative for values larger 180

        tile_position = (tile_direction, tile_magnitude)
        tile_dict[tile_position] = (tile_dict.get(tile_position, 0) + 1) % 2
    return tile_dict


def part_one(input_lines):
    return sum(flipping_tiles_from_line(input_lines).values())


def get_neightbors(tile, tile_pos):
    # from given tuple of direction and magnitude, reconstruct tile vector
    tile_vector = Vector(tile[1] * cos(radians(tile[0])), tile[1] * sin(radians(tile[0])))
    return_tile_dict = {}
    for adjecent in [EAST, WEST, NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST]:
        new_tile = tile_vector + adjecent
        new_tile_pos = (round(degrees(new_tile.direction()), 1), round(abs(new_tile), 1))
        return_tile_dict[new_tile_pos] = tile_pos.get(new_tile_pos, 0)
    return return_tile_dict


def part_two(starting_dict, iter_rounds):
    used_dict = deepcopy(starting_dict)
    for _ in range(iter_rounds):
        act_dict = deepcopy(used_dict)
        for n in [get_neightbors(tile, starting_dict) for tile in starting_dict]:
            for tile_pos, tile_val in n.items():
                if tile_pos not in act_dict.keys():
                    act_dict[tile_pos] = tile_val
        used_dict = deepcopy(act_dict)
        for tile_pos, tile_val in act_dict.items():
            neighbors = get_neightbors(tile_pos, act_dict)
            black_tiles = sum(neighbors.values())
            if tile_val == 1 and black_tiles in FLIP_TO_WHITE_RULE:
                starting_dict[tile_pos] = 0
            if tile_val == 0 and black_tiles in FLIP_TO_BLACK_RULE:
                starting_dict[tile_pos] = 1
    return sum(used_dict.values())


if __name__ == "__main__":
    print("Welcome to flipping_tiles.py")
    input_lines = load_input_file(os.getcwd())
    starting_dict = flipping_tiles_from_line(input_lines)
    print(part_one(input_lines))
    print(part_two(starting_dict, 100))
