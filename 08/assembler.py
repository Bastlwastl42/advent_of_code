#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 08/12/2020 07:18

@author: Sebastian

assembler.py is a script for advent of code day 8
"""

import os

from common import load_input_file
from typing import List
from copy import copy


def acc(act_line: int, accumulator, add_val: str):
    """
    Accumulate and return next line
    :param add_val:
    :return:
    """
    accumulator['act_val'] += int(add_val)
    #print(f'New acc value is {accumulator}')
    return act_line + 1


def nop(act_line: int, value: str):
    """
    Do nothing and return next line
    :param value:
    :return:
    """
    return act_line + 1


def jump(act_line: int, offset: str):
    """
    Do nothing and return next line according to offset
    :param offset:
    :return:
    """
    return act_line + int(offset)

def check_execution(programm: List[str]):
    """
    checks if the given programm terminates and returns accumulator dict
    :param programm:
    :return: bool, accumulator value
    """
    line_counter = 0
    list_of_executed_lines = [0]
    accumulator_value = {'act_val': 0}
    last_instruction = len(programm)
    while True:
        (command, value) = programm[line_counter]
        if command == 'nop':
            line_counter = nop(line_counter, value)
        if command == 'jmp':
            line_counter = jump(line_counter, value)
        if command == 'acc':
            line_counter = acc(line_counter, accumulator_value, value)
        if line_counter in list_of_executed_lines:
            print(
                f'Found first line visted twice! {line_counter} after {len(list_of_executed_lines)} operations')
            print(f'Accumulator value is {accumulator_value["act_val"]}')
            return False, accumulator_value
        else:
            list_of_executed_lines.append(line_counter)
        if line_counter == last_instruction:
            print('Found end of programm!')
            return True, accumulator_value



if __name__ == "__main__":
    print("Welcome to assembler.py")
    input_lines = [line.split(' ') for line in load_input_file(os.getcwd())]
    # part 1
    _, acc_value = check_execution(programm=input_lines)
    print(acc_value)

    # part 2
    for counter, (command, value) in enumerate(input_lines):
        replace_command = command
        if command == 'acc':
            continue
        if command == 'jmp':
            replace_command = 'nop'
        if command == 'nop':
            replace_command = 'jmp'
        next_program = copy(input_lines)
        next_program[counter] = (replace_command, value)
        success_run, acc_value = check_execution(next_program)
        if success_run:
            print(f'Found it, had to change line {counter} to {replace_command}')
            print(f'Accumulator value is {acc_value["act_val"]}')
            break
    print('Done')
