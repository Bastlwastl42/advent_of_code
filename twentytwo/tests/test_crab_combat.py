#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 22/12/2020 10:56

@author: Sebastian

test_crab_combat.py is a unittest for advetn of code 22
"""
import os
import unittest

from common import load_input_file
from twentytwo.crab_combat import deal_hands, play_crab_combat, get_score, \
    play_recursive_crab_combat


class TestCrabCombat(unittest.TestCase):
    def setUp(self) -> None:
        input_lines = load_input_file(os.getcwd(), 'test_input.txt')
        self.player_one, self.player_two = deal_hands(input_lines)

    def test_part_one(self):
        winnig_deck = play_crab_combat(self.player_one, self.player_two)
        self.assertListEqual([3, 2, 10, 6, 8, 5, 9, 4, 7, 1], winnig_deck)
        self.assertEqual(306, get_score(winnig_deck))
        winnig_deck = play_crab_combat(self.player_two, self.player_one)
        self.assertListEqual([3, 2, 10, 6, 8, 5, 9, 4, 7, 1], winnig_deck)
        self.assertEqual(306, get_score(winnig_deck))

    def test_part_two(self):
        winner, player_one_won = play_recursive_crab_combat(self.player_one, self.player_two)
        self.assertListEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3], winner)
        self.assertFalse(player_one_won)
        self.assertEqual(291, get_score(winner))
        winner, player_one_won = play_recursive_crab_combat(self.player_two, self.player_one)
        self.assertListEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3], winner)
        self.assertTrue(player_one_won)
        self.assertEqual(291, get_score(winner))


if __name__ == "__main__":
    unittest.main()
