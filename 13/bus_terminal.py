#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 13/12/2020 12:30

@author: Sebastian Lehrack

bus_terminal.py is a script for advent of code day 13
"""

import os

from common import load_input_file

BUS_LINE_OFFSET = [(counter, int(value)) for counter, value in
                   enumerate(load_input_file(os.getcwd())[1].split(',')) if
                   value != 'x']


def check_bus_line(time, offset_val):
    for offset, bus_line in offset_val:
        if (time + offset) % bus_line != 0:
            return 0
    return time


if __name__ == "__main__":
    print("Welcome to bus_terminal.py")

    input_lines = load_input_file(os.getcwd())

    act_time = int(input_lines[0])
    valid_bus_lines = [int(i) for i in input_lines[1].split(',') if i != 'x']

    time_counter = 0
    found_bus = False

    while not found_bus:
        for bus_line in valid_bus_lines:
            found_bus = ((act_time + time_counter) % bus_line == 0)
            if found_bus:
                print(f'Found time and busline! {bus_line}, wait for {time_counter}: '
                      f'{bus_line * time_counter}')
                break
        time_counter += 1

    # part two
    # starting with hint
    act_time = 100202913000000
    # act_time = 0
    time_counter = 0

    # valid solution must contain a mutliply of the max value
    # hence, correct offset to max and iter by this value

    max_val = max([v for _, v in BUS_LINE_OFFSET])
    [max_offset] = [o for o, v in BUS_LINE_OFFSET if v == max_val]
    new_offset_vals = [(offset - max_offset, value) for offset, value in BUS_LINE_OFFSET]

    while 1:
        if time_counter % 1000000 == 0:
            print(f'passing {time_counter + act_time}')

        if check_bus_line(act_time + time_counter, new_offset_vals):
            print(f'Found the time: {act_time + time_counter - max_offset}')
            break
        time_counter += max_val

    '''
    pool = Pool()
    not_found = True
    chunck_offset = 1000000 * time_counter_offset
    while not_found:
        print(f'passing {act_time + chunck_offset * time_counter}')
        next_chunck = [(act_time + chunck_offset * time_counter) + time_counter_offset * counter for
                       counter in range(0, chunck_offset, 1)]
        pool_return = pool.map(check_bus_line, next_chunck)
        act_found = any(pool_return)
        if act_found:
            print(f'Found the time: {[i for i in pool_return if i !=0][0]}')
            break
        time_counter += 1
    pool.close()

    while not found_time:
            if time_counter % 1000000 == 0:
                print(f'passing {time_counter + act_time}')
            found_time = all([(act_time + time_counter + offset) % bus_line == 0
                              for offset, bus_line in valid_bus_lines_offset])
            if found_time:
                print(f'Found the time: {act_time + time_counter}')
                break
            time_counter += time_counter_offset'''
