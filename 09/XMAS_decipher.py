#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 09/12/2020 08:02

@author: Sebastian

XMAS_decipher.py is a script for advent of code day 9
"""
import os
from typing import List

from common import load_input_file

SUBSET_LENGTH = 25


def find_sum_of_two(number: int, subset: List[int]):
    if len(subset) != SUBSET_LENGTH:
        print('INVALID SUBSET GIVEN: LENGTH!')
    return [summand for summand in subset if number - summand in subset]


if __name__ == "__main__":
    print("Welcome to XMAS_decipher.py")

    input_numbers = [int(i) for i in load_input_file(os.getcwd())]
    max_iter_val = len(input_numbers) - SUBSET_LENGTH - 1
    for counter in range(max_iter_val):
        findings = find_sum_of_two(number=input_numbers[counter + SUBSET_LENGTH],
                                   subset=input_numbers[counter:SUBSET_LENGTH + counter])
        if not findings:
            weakness_value = input_numbers[counter + SUBSET_LENGTH]
            print(weakness_value)
            break

    for low_counter in range(max_iter_val):
        found_set = []
        for up_counter in range(low_counter + 1, max_iter_val, 1):
            cur_sum = sum(input_numbers[low_counter:up_counter])
            if cur_sum < weakness_value:
                continue
            elif cur_sum > weakness_value:
                break
            elif cur_sum == weakness_value:
                print('Found set!')
                found_set = input_numbers[low_counter:up_counter]
                print(found_set)
                print(f'Min {min(found_set)} and Max {max(found_set)}')
                print(f'Sum is {min(found_set) + max(found_set)}')
                break
        if found_set:
            break

    print('Ende')
