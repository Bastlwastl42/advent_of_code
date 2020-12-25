#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 14:09

@author: Sebastian Lehrack

test_flipping_tiles.py is a unittest for advent of code day 24/
"""

import os
import unittest

from common import load_input_file
from twentyfour.flipping_tiles import flipping_tiles_from_line, get_tile_pos, SOUTH_EAST
from math import radians

class TestFlippingTiles(unittest.TestCase):

    def setUp(self) -> None:
        self.input_lines = load_input_file(os.getcwd(), 'test_input.txt')

    def test_directions(self):
        self.assertEqual((300, 1.0), get_tile_pos('esew'))
        self.assertEqual((0, 0), get_tile_pos('nwwswee'))

    def test_part_one(self):
        self.assertEqual(10, flipping_tiles_from_line(self.input_lines))
        real_input = load_input_file(os.path.join(os.getcwd(), '..'))
        self.assertEqual(485, flipping_tiles_from_line(real_input))


if __name__ == "__main__":
    unittest.main()
