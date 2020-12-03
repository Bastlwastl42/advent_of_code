#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 03/12/2020 08:51

@author: Sebastian Lehrack

rosselsprung.py is a script for advent of code part 3
"""
import os
from common import load_input_file
from math import prod

TREE_SIGN = '#'
FREE_SIGN = '.'

MOVING_PATERNS = [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)]

def follow_patterns(input_lines, down_inc, right_inc):
    tree_counter = 0
    max_width = len(input_lines[0])
    print(f'Checking paterns {down_inc} down, {right_inc} right... ', end='')
    for (depth_counter, line_counter) in zip(
            range(1 * down_inc - 1 * down_inc, len(input_lines), down_inc),
            range(len(input_lines))):
        #print(f'{depth_counter}, {(line_counter * right_inc)}')
        if input_lines[depth_counter][((line_counter * right_inc) % max_width)] == TREE_SIGN:
            # print(f'Hit tree at {depth_counter}')
            tree_counter += 1
    print(f'{tree_counter}')
    return tree_counter


if __name__ == "__main__":
    print("Welcome to rosselsprung.py")
    input_lines = load_input_file(os.getcwd())
    max_width = len(input_lines[0])
    max_depth = len(input_lines)
    print(f'{max_width}x{max_depth}')
    tree_encounters = [follow_patterns(input_lines, down, right) for down, right in MOVING_PATERNS]
    print(f'Part one: Encountered {tree_encounters[0]} trees.')
    print(f'Part two: the product of all encounters is {prod(tree_encounters)}')
