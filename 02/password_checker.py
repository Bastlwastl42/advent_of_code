#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 02/12/2020 08:23

@author: Sebastian Lehrack

password_checker.py is a script for advent of code part 02
"""
import os
from common import load_input_file
from typing import List


def line_split(line):
    rule, password = line.split(': ')
    letter_for_rule = rule.split(' ')[-1]
    min_rule, max_rule = [int(e) for e in rule.split(' ')[0].split('-')]
    return (min_rule, max_rule, letter_for_rule, password)


if __name__ == "__main__":
    print("Welcome to password_checker.py")
    input_list = load_input_file(folder=os.getcwd())

    check_pw_part_one: List[bool] = []
    for min_rule, max_rule, letter_for_rule, password in [line_split(e) for e in input_list]:
        # print(f'{min_rule}, {max_rule}, {letter_for_rule}, {password}')
        letter_account = sum([1 for e in password if e == letter_for_rule])
        password_valid = (min_rule <= letter_account <= max_rule)
        # print(password_valid)
        check_pw_part_one.append(password_valid)
    print(f'Part one: Number of Valid Passwords: {len([e for e in check_pw_part_one if e])}')

    check_pw_part_two: List[bool] = []
    for first_encounter, second_encounter, letter_for_rule, password \
            in [line_split(e) for e in input_list]:
        check_pw_part_two.append((password[first_encounter-1] == letter_for_rule)
                                 ^ (password[second_encounter-1] == letter_for_rule))
    print(f'Part two: Number of valid passwords: {len([e for e in check_pw_part_two if e])}')
