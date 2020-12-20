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
from seventeen.satelite_bootup import SateliteSimulation

SOLUTION_TEST_PART_ONE = 112
SOLUTION_TEST_PART_TWO = 848

class TestSeventeen(unittest.TestCase):

    def test_part_one(self):
        my_sim_sat = SateliteSimulation(load_input_file(os.getcwd(), 'test_input.txt'), 3)
        self.assertEqual(my_sim_sat.boot_up_(), SOLUTION_TEST_PART_ONE)

    def test_part_two(self):
        my_sim_sat = SateliteSimulation(load_input_file(os.getcwd(), 'test_input.txt'), 4)
        self.assertEqual(my_sim_sat.boot_up_(), SOLUTION_TEST_PART_TWO)


if __name__ == "__main__":
    unittest.main()
