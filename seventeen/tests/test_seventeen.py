#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 17/12/2020 08:14

@author: Sebastian Lehrack

test_seventeen.py is a script for....
"""
import os
import unittest
from common import load_input_file
from seventeen.satelite_bootup import boot_up_part_one

SOLUTION_TEST_PART_ONE = 112

class TestSeventeen(unittest.TestCase):

    def test_part_one(self):
        input_lines = load_input_file(os.getcwd(), 'test_input.txt')
        self.assertEqual(boot_up_part_one(input_lines), SOLUTION_TEST_PART_ONE)


if __name__ == "__main__":
    unittest.main()
