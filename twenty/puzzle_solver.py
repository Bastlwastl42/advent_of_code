#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 22/12/2020 12:49

@author: Sebastian

puzzle_solver.py is a script for advent of code day 20
"""

import math
import os
from typing import List, Dict

from common import load_input_file


class PuzzlePiece:
    def __init__(self, tile_number, tile_input):
        self.tile_number = tile_number
        self.tile_input = tile_input
        self.border_up = list(self.tile_input[0])
        self.border_down = list(self.tile_input[-1])
        self.border_left = [i[0] for i in self.tile_input]
        self.border_right = [i[-1] for i in self.tile_input]
        self.oritentation = (1, 0)
        self.flipped = (1, 1)  # not flipped in/around (H, V) direction. Flipping would turn to -1
        self.borders = [self.border_up, self.border_right, self.border_down, self.border_left]

    def get_borders(self):
        self.borders = [self.border_up, self.border_right, self.border_down, self.border_left]
        return self.borders

    def flip_borders(self, orientation):
        if orientation == 'H':
            # flip around horizontal axis
            self.flipped[0] *= -1
            self.border_left = reversed(self.border_left)
            self.border_right = reversed(self.border_right)
            swap = self.border_down
            self.border_down = self.border_up
            self.border_up = swap

        if orientation == 'V':
            # flip around vertical axis
            self.flipped[1] *= -1
            swap = self.border_right
            self.border_right = self.border_left
            self.border_left = swap
            self.border_up = reversed(self.border_up)
            self.border_down = reversed(self.border_down)

    def rotate_borders(self, direction):
        swap = self.border_up
        if direction == 'L':
            # rotate counter clockwise
            self.orientation = [e - math.cos(math.pi * e) for e in self.oritentation]
            self.border_up = self.border_right
            self.border_right = self.border_down
            self.border_down = self.border_left
            self.border_left = swap

        if direction == 'R':
            self.orientation = [e + math.cos(math.pi * e) for e in self.oritentation]
            self.border_up = self.border_left
            self.border_left = self.border_down
            self.border_down = self.border_right
            self.border_right = swap
        self.borders = self.get_borders()

class Puzzle:

    def __init__(self, input_parts):
        self.part_dict = {}
        for part in input_parts:
            splitted_parts = part.split(':')
            tile_id = int(splitted_parts[0].split(' ')[1])
            tile = splitted_parts[1].lstrip().split('\n')
            act_part = PuzzlePiece(tile_id, tile)
            self.part_dict[act_part] = []

    def find_matches(self):
        pass


def load_input(filename='input.txt', folder=os.getcwd()):
    with open(os.path.join(folder, filename)) as f:
        input = f.read()
    return input.split('\n\n')


def solve_puzzle(puzzle_dict: Dict):
    pass


def create_puzzle_dict(input_lines: List[str]) -> Dict:
    pass


if __name__ == "__main__":
    print("Welcome to puzzle_solver.py")
    parts = load_input()
    my_puzzle = Puzzle(parts)
    print(solve_puzzle(create_puzzle_dict(load_input_file(os.getcwd()))))
