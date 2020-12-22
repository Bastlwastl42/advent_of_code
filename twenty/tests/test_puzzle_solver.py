#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 22/12/2020 12:51

@author: Sebastian Lehrack

test_puzzle_solver.py is a script for....
"""

import unittest
import os
from common import load_input_file
from twenty.puzzle_solver import solve_puzzle, create_puzzle_dict
class TestPuzzleSolver(unittest.TestCase):
    def setUp(self) -> None:
        input_lines = load_input_file(os.getcwd(), 'test_input.txt')
        self.puzzle_dict = create_puzzle_dict(input_lines)

    def test_part_one(self):
        """
        Solution part one:
        1951    2311    3079
        2729    1427    2473
        2971    1489    1171
        result is product of edge tiles
        """
        self.assertEqual(solve_puzzle(self.puzzle_dict), 20899048083289)


if __name__ == "__main__":
    print("Welcome to test_puzzle_solver.py")

