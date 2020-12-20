#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 16/12/2020 08:39

@author: Sebastian

test_sixten.py: unittesting advent of code part 16
"""

import unittest
import os
from sixteen.train_ticket_checker import check_error_codes
from common import load_input_file

class TestDaySixteen(unittest.TestCase):
    def test_part_1(self):
        input = load_input_file(os.getcwd(), 'test_input.txt')
        self.assertEqual(check_error_codes(input), 71)


if __name__ == "__main__":
    unittest.main()
