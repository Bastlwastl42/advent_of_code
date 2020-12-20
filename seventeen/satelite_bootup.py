#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 17/12/2020 08:16

@author: Sebastian

satelite_bootup.py is a script for advent of code day 17
"""
import itertools
import os
from copy import deepcopy
from typing import Dict

from common import load_input_file

ACTIVE_SIGN = '#'
INACTIVE_SIGN = '.'
ACTIVE_VALUE = 1
INACTIVE_VALUE = 0


class SateliteSimulation:

    def __init__(self, input_lines, dimension):
        self.set_field_dict = {}
        self.dimension = dimension
        # if active and neighbors are in this list, stay active
        self.continue_living = [2, 3]
        # if inactive and this number of neighbors is active, become active
        self.start_living = [3]
        initial_vals = [0 for _ in range(self.dimension)]
        for x_counter, line in enumerate(input_lines):
            for y_counter, val in enumerate(line):
                field_id = initial_vals
                field_id[0] = x_counter
                field_id[1] = y_counter
                if val == ACTIVE_SIGN:
                    self.set_field_dict[tuple(field_id)] = ACTIVE_VALUE
                if val == INACTIVE_SIGN:
                    self.set_field_dict[tuple(field_id)] = INACTIVE_VALUE

    def update_field(self):
        """make one roundtrip through all fields"""
        field_dict_copy = deepcopy(self.set_field_dict)
        for field_id, value in self.set_field_dict.items():
            living_neighbors = self.get_neighbor(field_id).values()
            if value == ACTIVE_VALUE:
                if sum(living_neighbors) in self.continue_living:
                    continue
                else:
                    field_dict_copy[field_id] = INACTIVE_VALUE
            if value == INACTIVE_VALUE:
                if sum(living_neighbors) in self.start_living:
                    field_dict_copy[field_id] = ACTIVE_VALUE
        self.set_field_dict = field_dict_copy

    def fill_in_neighbors(self):
        field_dict_copy = deepcopy(self.set_field_dict)
        # extend current field by all possible neighbors
        for field_id, value in self.set_field_dict.items():
            neighbors = self.get_neighbor(field_id)
            for e, n in neighbors.items():
                field_dict_copy[e] = n
        self.set_field_dict = field_dict_copy

    def get_all_living(self):
        return sum(self.set_field_dict.values())

    def get_neighbor(self, field_tuple) -> Dict:
        product_lists = []
        for counter in range(self.dimension):
            product_lists.append(
                [field_tuple[counter] - 1, field_tuple[counter], field_tuple[counter] + 1])
        return {e: self.set_field_dict.get(e, INACTIVE_VALUE) for e in
                itertools.product(*product_lists)
                if e != field_tuple}


    def boot_up_(self):
        boot_up_cycles = 6
        for counter in range(boot_up_cycles):
            print('.', end='')
            self.fill_in_neighbors()
            self.update_field()
        return self.get_all_living()


if __name__ == "__main__":
    print("Welcome to satelite_bootup.py")
    # part one
    input_lines = load_input_file(os.getcwd())
    my_sim_sat_part_one = SateliteSimulation(input_lines, 3)
    print('Running part One', end='')
    print(my_sim_sat_part_one.boot_up_())
    # part two
    print('Running part Two', end='')
    my_sim_sat_part_two = SateliteSimulation(input_lines, 4)
    print(my_sim_sat_part_two.boot_up_())
