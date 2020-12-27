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
from twentyfour.flipping_tiles import flipping_tiles_from_line, get_tile_pos, part_one, part_two


class TestFlippingTiles(unittest.TestCase):

    def setUp(self) -> None:
        self.input_lines = load_input_file(os.getcwd(), 'test_input.txt')
        self.starting_dict = flipping_tiles_from_line(self.input_lines)

    def test_directions(self):
        self.assertEqual((300, 1.0), get_tile_pos('esew'))
        self.assertEqual((0, 0), get_tile_pos('nwwswee'))

    def test_part_one(self):
        self.assertEqual(10, part_one(self.input_lines))
        real_input = load_input_file(os.path.join(os.getcwd(), '..'))
        self.assertEqual(485, part_one(real_input))

    def test_part_two(self):
        """
        Day 1: 15
        Day 2: 12
        Day 3: 25
        Day 4: 14
        Day 5: 23
        Day 6: 28
        Day 7: 41
        Day 8: 37
        Day 9: 49
        Day 10: 37

        Day 20: 132
        Day 30: 259
        Day 40: 406
        Day 50: 566
        Day 60: 788
        Day 70: 1106
        Day 80: 1373
        Day 90: 1844
        Day 100: 2208
        :return:
        """
        test_results = [(1, 15),
                        (2, 12),
                        (3, 25),
                        (4, 14),
                        (5, 23),
                        (6, 28),
                        (7, 41),
                        (8, 37),
                        (9, 49),
                        (10, 37),
                        (20, 132),
                        (30, 259),
                        (40, 406),
                        (50, 566),
                        (60, 788),
                        (70, 1106),
                        (80, 1373),
                        (90, 1844),
                        (100, 2208)]
        for rounds, result in test_results:
            with self.subTest(f'Testing for {rounds}, expecting {result}',
                              rounds=rounds, result=result):
                self.assertEqual(result, part_two(self.starting_dict, rounds))


if __name__ == "__main__":
    unittest.main()
