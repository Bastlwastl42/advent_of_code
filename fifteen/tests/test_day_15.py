#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 15/12/2020 07:57

@author: Sebastian Lehrack

test_day_15.py is a script for....
"""

import os
import unittest

from common import load_input_file
from fifteen.elves_memory_game import gimme_number_twenty_twenty


class TestDay15(unittest.TestCase):
    def setUp(self) -> None:
        input_lines = [line.split(':') for line in load_input_file(os.getcwd(), 'input_test.txt')]
        self.given_correct_answers_2020 = {}
        for starting_numbers, solution in input_lines:
            self.given_correct_answers_2020[int(solution)] = [int(i) for i in
                                                              starting_numbers.split(',')]

        input_lines = [line.split(':') for line in
                       load_input_file(os.getcwd(), 'input_test_30much.txt')]
        self.given_correct_answers_30much = {}
        for starting_numbers, solution in input_lines:
            self.given_correct_answers_30much[int(solution)] = [int(i) for i in
                                                                starting_numbers.split(',')]

    def test_gimme_twentytwenty(self):
        for solution, starting_numbers in self.given_correct_answers_2020.items():
            with self.subTest(f'Testing {starting_numbers}, expecting {solution}'):
                self.assertEqual(gimme_number_twenty_twenty(starting_numbers, 2020), solution)

    def test_gimme_30much(self):
        for solution, starting_numbers in self.given_correct_answers_30much.items():
            with self.subTest(f'Testing {starting_numbers}, expecting {solution}'):
                self.assertEqual(gimme_number_twenty_twenty(starting_numbers, 30000000), solution)


if __name__ == "__main__":
    unittest.main(TestDay15)
