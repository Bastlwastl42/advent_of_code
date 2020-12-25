#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 14:09

@author: Sebastian Lehrack

test_flipping_tiles.py is a unittest for advent of code day 24/
"""

import unittest
import os
from common import load_input_file
from twentyfour import flipping_tiles


class TestFlippingTiles(unittest.TestCase):

    def setUp(self) -> None:
        self.input_lines = load_input_file(os.getcwd(), 'test_input.txt')

    def test_part_one(self):
        self.assertEqual(10, flipping_tiles(self.input_lines))


if __name__ == "__main__":
    unittest.main()
