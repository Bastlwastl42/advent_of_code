#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 26/12/2020 13:10

@author: Sebastian

test_twentyFive is a script for unit testing advent of code day 25
"""
import unittest

from twentyfive.fun_with_encryptions import get_loop_number, get_encryption_key


class TestTwentyFive(unittest.TestCase):

    def test_get_loop_number(self):
        self.assertEqual(8, get_loop_number(5764801))
        self.assertEqual(11, get_loop_number(17807724))

    def test_get_encryption_key(self):
        self.assertEqual(14897079, get_encryption_key(17807724, 8))
        self.assertEqual(14897079, get_encryption_key(5764801, 11))
        self.assertEqual(get_encryption_key(5764801, 11), get_encryption_key(17807724, 8))


if __name__ == "__main__":
    unittest.main()
