#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 17/12/2020 08:16

@author: Sebastian

satelite_bootup.py is a script for advent of code day 17
"""
import itertools
import os

from common import load_input_file

ACTIVE_SIGN = '#'
INACTIVE_SIGN = '.'


class SateliteSimulation:

    def __init__(self, input_lines):
        self.set_field_dict = {}
        inital_z = 0
        for x_counter, line in enumerate(input_lines):
            for y_counter, val in enumerate(line):
                if val == ACTIVE_SIGN:
                    self.set_field_dict[(x_counter, y_counter, inital_z)] = 1
                if val == INACTIVE_SIGN:
                    self.set_field_dict[(x_counter, y_counter, inital_z)] = 0

    def update_field(self):
        pass

    def fill_in_neighbors(self):
        pass

    def get_neighbor(self, x, y, z):
        return [self.set_field_dict.get(e, INACTIVE_SIGN) for e in
                itertools.product([x - 1, x, x + 1], [y - 1, y, y + 1], [z - 1, z, z + 1]) if e != (x, y, z)]


def boot_up_part_one(input_lines):
    pass


if __name__ == "__main__":
    print("Welcome to satelite_bootup.py")
    # part one
    boot_up_part_one(load_input_file(os.getcwd()))
