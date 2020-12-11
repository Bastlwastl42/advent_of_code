#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 11/12/2020 08:04

@author: Sebastian

ising_model_seats.py is a script for advent of code 11
"""

import os

from common import load_input_file
from copy import deepcopy

EMPTY_SEAT = bytearray('L', 'utf-8')[0]
FLOOR = bytearray('.', 'utf-8')[0]
OCCUPIED_SEAT = bytearray('#', 'utf-8')[0]


def get_full_square(input_lines, x, y):
    max_depth = len(input_lines)
    max_line = len(input_lines[0])
    # cover edge cases
    if x == 0 and y == 0:
        return [FLOOR, FLOOR, FLOOR,
                FLOOR, input_lines[x][y], input_lines[x + 1][y],
                FLOOR, input_lines[x][y + 1], input_lines[x + 1][y + 1]]
    if x == max_depth - 1 and y == max_line - 1:
        return [input_lines[x - 1][y - 1], input_lines[x][y - 1], FLOOR,
                input_lines[x - 1][y], input_lines[x][y], FLOOR,
                FLOOR, FLOOR, FLOOR]
    if x == 0 and y == max_line - 1:
        return [FLOOR, input_lines[x][y - 1], input_lines[x + 1][y - 1],
                FLOOR, input_lines[x][y], input_lines[x + 1][y],
                FLOOR, FLOOR, FLOOR]
    if x == max_depth - 1 and y == 0:
        return [FLOOR, FLOOR, FLOOR,
                input_lines[x - 1][y], input_lines[x][y], FLOOR,
                input_lines[x - 1][y + 1], input_lines[x][y + 1], FLOOR]
    if x == 0 and y not in [0, max_line]:
        try:
            return [FLOOR, input_lines[x][y - 1], input_lines[x + 1][y - 1],
                    FLOOR, input_lines[x][y], input_lines[x + 1][y],
                    FLOOR, input_lines[x][y + 1], input_lines[x + 1][y + 1]]
        except IndexError:
            print('what')
    if x == max_depth - 1 and y not in [0, max_line - 1]:
        return [input_lines[x - 1][y - 1], input_lines[x][y - 1], FLOOR,
                input_lines[x - 1][y], input_lines[x][y], FLOOR,
                input_lines[x - 1][y + 1], input_lines[x][y + 1], FLOOR]
    if y == 0 and x not in [0, max_depth - 1]:
        return [FLOOR, FLOOR, FLOOR,
                input_lines[x - 1][y], input_lines[x][y], input_lines[x + 1][y],
                input_lines[x - 1][y + 1], input_lines[x][y + 1], input_lines[x + 1][y + 1]]
    if y == max_line - 1 and x not in [0, max_depth - 1]:
        return [input_lines[x - 1][y - 1], input_lines[x][y - 1], input_lines[x + 1][y - 1],
                input_lines[x - 1][y], input_lines[x][y], input_lines[x + 1][y],
                FLOOR, FLOOR, FLOOR]

    return [input_lines[x - 1][y - 1], input_lines[x][y - 1], input_lines[x + 1][y - 1],
            input_lines[x - 1][y], input_lines[x][y], input_lines[x + 1][y],
            input_lines[x - 1][y + 1], input_lines[x][y + 1], input_lines[x + 1][y + 1]]


def get_all_occ_seats(input_lines):
    return sum([1 for line in input_lines for e in line if e == OCCUPIED_SEAT])


def seat_not_occupied(seat_val: str):
    if seat_val in [EMPTY_SEAT, FLOOR]:
        return True
    return False


def surrounding(square_val):
    return [i for counter, i in enumerate(square_val) if counter != 4]


def convert_to_occupied(square_val):
    surround = surrounding(square_val)
    if square_val[4] == EMPTY_SEAT and all([seat_not_occupied(i) for i in surround]):
        return OCCUPIED_SEAT
    return square_val[4]


def convert_to_empty(square_val):
    surround = surrounding(square_val)
    if square_val[4] == OCCUPIED_SEAT and sum([1 for i in surround if i == OCCUPIED_SEAT]) >= 4:
        return EMPTY_SEAT
    return square_val[4]


if __name__ == "__main__":
    print("Welcome to ising_model_seats.py")
    input_vals = [bytearray(line, 'utf-8') for line in load_input_file(os.getcwd())]
    # print(input_lines)
    same_occupation = True
    max_depth = len(input_vals)
    max_line = len(input_vals[0])
    iter_counter = 0
    new_vals = deepcopy(input_vals)
    while same_occupation:
        previous_occupied = get_all_occ_seats(input_vals)
        for x in range(max_depth):
            for y in range(max_line):
                new_vals[x][y] = convert_to_occupied(get_full_square(input_vals, x, y))

        for x in range(max_depth):
            for y in range(max_line):
                input_vals[x][y] = convert_to_empty(get_full_square(new_vals, x, y))
        iter_counter += 1
        current_occupation = get_all_occ_seats(input_vals)
        same_occupation = not (current_occupation == previous_occupied)
        print(
            f'Iteration {iter_counter}: prev: {previous_occupied}, curr: {current_occupation}')
