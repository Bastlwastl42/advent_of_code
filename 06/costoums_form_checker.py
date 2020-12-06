#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 06/12/2020 10:50

@author: Sebastian

costoums_form_checker.py is a script for advent of code day 6
"""
import os
from common import load_input_file
from string import ascii_lowercase

if __name__ == "__main__":
    print("Welcome to costoums_form_checker.py")

    input_lines = '\n'.join(load_input_file(os.getcwd())).split('\n\n')
    answers_per_group = []
    #part one
    for line in input_lines:
        group_answers = {e for person_answer in line.split('\n') for e in person_answer}
        answers_per_group.append(len(group_answers))
    print(sum(answers_per_group))

    #part two
    group_all_yes_answers = []
    for line in input_lines:
        group_answers = set(ascii_lowercase)
        for person_answer in line.split('\n'):
            group_answers = group_answers.intersection({e for e in person_answer})
        group_all_yes_answers.append(len(group_answers))
    print(sum(group_all_yes_answers))
