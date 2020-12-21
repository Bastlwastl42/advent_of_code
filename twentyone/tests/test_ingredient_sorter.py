#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 21/12/2020 10:40

@author: Sebastian Lehrack

test_ingredient_sorter.py is a script for....
"""
import unittest
import os
from common import load_input_file
from twentyone.ingredient_sorter import part_two, part_one


class TestIngredientSorter(unittest.TestCase):

    def setUp(self) -> None:
        self.input_lines = [line.split('(contains ') for line in
                   load_input_file(os.getcwd(), 'test_input.txt')]

    def test_part_one(self):
        self.assertEqual(part_one(self.input_lines), 5)

    def test_part_two(self):
        self.assertEqual(part_two(self.input_lines), 'mxmxvkd,sqjhc,fvjkl')


if __name__ == "__main__":
    print("Welcome to test_ingredient_sorter.py")

