#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 20/12/2020 16:14

@author: Sebastian

test_eightteen.py is a unittest for advent of code day 18
"""
import unittest

from eightteen.recursion_overload import evaluate_expression, evaluate_expression_part_two


class TestEightteen(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(evaluate_expression('1 + 2 * 3 + 4 * 5 + 6'.split(' ')), 71)
        self.assertEqual(evaluate_expression('1 + (2 * 3) + (4 * (5 + 6))'.split(' ')), 51)
        self.assertEqual(evaluate_expression('2 * 3 + (4 * 5)'.split(' ')), 26)
        self.assertEqual(evaluate_expression('5 + (8 * 3 + 9 + 3 * 4 * 3)'.split(' ')), 437)
        self.assertEqual(evaluate_expression('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'.split(' ')), 12240)
        self.assertEqual(evaluate_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.split(' ')),13632)

    def test_part_two(self):
        self.assertEqual(evaluate_expression_part_two('1 + 2 * 3 + 4 * 5 + 6'.split(' ')), 231)
        self.assertEqual(evaluate_expression_part_two('1 + (2 * 3) + (4 * (5 + 6))'.split(' ')), 51)
        self.assertEqual(evaluate_expression_part_two('2 * 3 + (4 * 5)'.split(' ')), 46)
        self.assertEqual(evaluate_expression_part_two('5 + (8 * 3 + 9 + 3 * 4 * 3)'.split(' ')), 1445)
        self.assertEqual(
            evaluate_expression_part_two('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'.split(' ')), 669060)
        self.assertEqual(
            evaluate_expression_part_two('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.split(' ')),
            23340)


if __name__ == "__main__":
    unittest.main()
