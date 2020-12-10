#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 10/12/2020 08:11

@author: Sebastian

jotage_adpaters.py is a script for advent of code day 10
"""
import math
import os
from typing import List

from common import load_input_file


def find_next_drei(counter: int, list_of_diffs: List[int]):
    for next_count, val in enumerate(list_of_diffs[counter + 1:]):
        if val == 3:
            return next_count
    return len(list_of_diffs[counter+1:])


def get_kombinations(n: int):
    if n in [0, 1]:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 7
    if n == 5:
        return 13
    raise ValueError


if __name__ == "__main__":
    print("Welcome to jotage_adpaters.py")

    input_number_sorted = [int(i) for i in load_input_file(os.getcwd(), file='input.txt')]
    input_number_sorted.append(0)
    input_number_sorted.append(max(input_number_sorted) + 3)
    input_number_sorted.sort()
    differences = [input_number_sorted[counter + 1] - input_number_sorted[counter] for counter in
                   range(len(input_number_sorted) - 1)]
    eins_jolt_diff = len([i for i in differences if i == 1])
    drei_jolt_diff = len([i for i in differences if i == 3])
    print(f'Found 1 jolt differences {eins_jolt_diff}, 3 jolt differences {drei_jolt_diff}, '
          f'Product {eins_jolt_diff * drei_jolt_diff}')
    # in the set of differences, find sequence pattern
    list_of_kombination = [get_kombinations(find_next_drei(0, differences)+1)]
    for counter, diff in enumerate(differences):
        if diff == 1:
            continue
        if diff == 3:
            list_of_kombination.append(get_kombinations(find_next_drei(counter, differences)))

    print(f'Part two provided {math.prod(list_of_kombination)}')
