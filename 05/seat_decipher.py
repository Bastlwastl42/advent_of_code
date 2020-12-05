#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 05/12/2020 10:34

@author: Sebastian

seat_decipher.py is a script for advent of code part 5.
"""

import os
from common import load_input_file


def decipher_line(line_input):
    row_val = sum(
        [pow(2, counter) for counter, val in enumerate(reversed(line_input[:7])) if val == 'B'])
    col_val = sum(
        [pow(2, counter) for counter, val in enumerate(reversed(line_input[7:])) if val == 'R'])
    return row_val, col_val


def get_seat_id(row_col):
    return row_col[0] * 8 + row_col[1]


if __name__ == "__main__":
    print("Welcome to seat_decipher.py")

    input_lines = load_input_file(os.getcwd())
    '''# check from given examples
    #input_lines.extend(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'])
    #print(input_lines)
    # for debugging
    for line in input_lines:
        (row, col) = decipher_line(line)
        print(f'{line[:7]} and {line[7:]}: ', end='')
        print(f'This is row {row} and col {col}. ', end='')
        print(f'This is seat ID {get_seat_id((row, col))}')'''
    list_of_seats = sorted([get_seat_id(decipher_line(line)) for line in input_lines])
    print(max(list_of_seats))
    for counter, e in enumerate(list_of_seats):
        if e+1 == list_of_seats[counter+1]:
            continue
        if list_of_seats[counter+1]-2 == e:
            print(f'Found your seat at {e+1}')
            break
        print('false alarm')
