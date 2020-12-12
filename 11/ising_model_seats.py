#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 11/12/2020 08:04

@author: Sebastian

ising_model_seats.py is a script for advent of code 11
"""

import os
from copy import deepcopy

from common import load_input_file

EMPTY_SEAT = bytearray('L', 'utf-8')[0]
FLOOR = bytearray('.', 'utf-8')[0]
OCCUPIED_SEAT = bytearray('#', 'utf-8')[0]
PART_TWO_FLAG = False
if PART_TWO_FLAG:
    OCCUPIED_TOLERANCE = 5
else:
    OCCUPIED_TOLERANCE = 4

DIRECTIONS = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (1, -1), (1, 0), (1, 1)]


def get_surrounds(input_lines, x, y):
    return_square = []
    for dir_x, dir_y in DIRECTIONS:
        if dir_x < 0:
            x_range = range(x + dir_x, 0 + dir_x, dir_x)
        if dir_x > 0:
            x_range = range(x + dir_x, max_depth, dir_x)
        if dir_y < 0:
            y_range = range(y + dir_y, 0 + dir_y, dir_y)
        if dir_y > 0:
            y_range = range(y + dir_y, max_line, dir_y)
        if dir_y == 0 and dir_x == 0:
            return_square.append(input_lines[x][y])
            continue
        if dir_x == 0:
            x_range = [x for _ in range(len(y_range))]
        if dir_y == 0:
            y_range = [y for _ in range(len(x_range))]

        found_seat = False
        for get_x, get_y in zip(x_range, y_range):
            if input_lines[get_x][get_y] == FLOOR and PART_TWO_FLAG:
                continue
            return_square.append(input_lines[get_x][get_y])
            found_seat = True
            break

        if not found_seat:
            return_square.append(FLOOR)
    return return_square


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
    if square_val[4] == OCCUPIED_SEAT and sum(
            [1 for i in surround if i == OCCUPIED_SEAT]) >= OCCUPIED_TOLERANCE:
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
                new_vals[x][y] = convert_to_occupied(get_surrounds(input_vals, x, y))

        for x in range(max_depth):
            for y in range(max_line):
                input_vals[x][y] = convert_to_empty(get_surrounds(new_vals, x, y))
        iter_counter += 1
        current_occupation = get_all_occ_seats(input_vals)
        same_occupation = not (current_occupation == previous_occupied)
        print(
            f'Iteration {iter_counter}: prev: {previous_occupied}, curr: {current_occupation}')
