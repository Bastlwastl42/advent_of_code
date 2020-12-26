#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 23/12/2020 19:57

@author: Sebastian

test_krabben_huetchenspiel.py is a script for unittest advent of code day 21
"""

import unittest
from twentythree.Kraben_Huetchenspiel import shufle_cups, get_starting_positions, get_million_starting_positions
from twentythree.kraben_huetchenspiel_part_two import KrabenHutchenspiel

class TestHuetchenspiel(unittest.TestCase):

    def test_part_one(self):
        starting_numbers = get_starting_positions('389125467')
        self.assertEqual([6,7,3,8,4,5,2,9], shufle_cups(starting_numbers))

    def test_part_two(self):
        starting_numbers = get_million_starting_positions('389125467')
        final_values = shufle_cups(starting_numbers, 10000000)
        self.assertEqual(934001, final_values[0])
        self.assertEqual(159792, final_values[-1])
        self.assertEqual(149245887792, final_values[-1]*final_values[0])


class TestHutchenspielPartTwo(unittest.TestCase):

    def test_part_one(self):
        starting_numbers = get_starting_positions('389125467')
        current_game = KrabenHutchenspiel(starting_numbers)
        self.assertEqual([6, 7, 3, 8, 4, 5, 2, 9], current_game.shuffle_cups(100))

    def test_part_two(self):
        starting_numbers = get_million_starting_positions('389125467')
        current_game = KrabenHutchenspiel(starting_numbers)
        current_game.shuffle_cups(10000000)
        one = current_game.get_value_entry(1)
        self.assertEqual(934001, one['next'])
        self.assertEqual(159792, current_game.get_value_entry(934001)['next'])
        self.assertEqual(149245887792, current_game.get_part_two())

if __name__ == "__main__":
    unittest.main()
