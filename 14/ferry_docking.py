#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 14/12/2020 07:40

@author: Sebastian

ferry_docking.py is a script for advetn of code 14
"""
import os

from common import load_input_file


def bitfield(n):
    return [1 if digit == '1' else 0 for digit in bin(int(n))[2:]]


def int_from_bit(bit_val):
    return sum([pow(2, exp) * field for exp, field in enumerate(reversed(bit_val))])


class MemoryWriter:

    def __init__(self):
        self.mask = ['X' for _ in range(32)]
        # memory is represented by address (key) and value
        self.memory = {}

    def set_mask(self, new_mask):
        self.mask = new_mask

    def apply_mask(self, mem_value):
        # convert value to bit for mask operations
        bit_values = bitfield(mem_value)
        extended_bit_values = [0 for _ in range(len(self.mask)-len(bit_values))]
        extended_bit_values.extend(bit_values)
        new_value = []
        for mask_val, bit_val in zip(self.mask, extended_bit_values):
            if mask_val == 'X':
                new_value.append(bit_val)
            else:
                new_value.append(int(mask_val))
        return int_from_bit(new_value)

    def write_new_value(self, address, value):
        new_value = self.apply_mask(value)
        self.memory[address] = new_value

    def sum_all_up(self):
        return sum([v for v in self.memory.values()])


if __name__ == "__main__":
    print("Welcome to ferry_docking.py")
    input_lines_splitted = [s.split(' = ') for s in load_input_file(os.getcwd())]
    my_memory = MemoryWriter()
    for command, value in input_lines_splitted:
        if command == 'mask':
            my_memory.set_mask(value)
            continue
        # better use re next time
        mem_address = int(command[4:-1])
        my_memory.write_new_value(mem_address, value)

    print(my_memory.sum_all_up())
