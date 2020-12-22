#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 21/12/2020 13:12

@author: Sebastian Lehrack

test_pattern_matching.py is a script for....
"""
import os
import unittest
from common import load_input_file

from nineteen.pattern_matching import part_one, part_two, split_rules

class TestPatternMatching(unittest.TestCase):

    def setUp(self) -> None:
        self.rules, self.messages = split_rules(load_input_file(os.getcwd(), 'test_input.txt'))

    def test_part_one(self):
        self.assertEqual(part_one(self.rules, self.messages), 2)


if __name__ == "__main__":
    unittest.main()

