#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 21/12/2020 13:12

@author: Sebastian

pattern_matching.py is a script for advent of code 19
"""
import os
import re
from itertools import product

from common import load_input_file

number_matching = re.compile('\d')


def part_one(rules, messages):
    rules_list = setup_rules(rules)


def part_two(rules, messages):
    pass


def split_rules(input_lines):
    for counter, line in enumerate(input_lines):
        if line == '':
            return [line.split(':') for line in input_lines[:counter]], input_lines[counter + 1:]
    raise ValueError


def setup_rules(rules):
    implicit_rules_dict = {counter: rule.lstrip() for counter, rule in rules}
    explicit_rules_dict = {}
    # try making rules explicit
    zero_rule = implicit_rules_dict['0']
    print(make_rule_explicit(zero_rule, implicit_rules_dict))
    print('something')


def make_rule_explicit(implicit_rule, rules_dict):
    if not number_matching.match(implicit_rule):
        return implicit_rule
    subrules = implicit_rule.split(' | ')
    final_rule = []
    for subrule in subrules:
        if len(subrule) == 1:
            return rules_dict[subrules[0]].replace('"', '')
        sub_final_rule = []
        for subrule in number_matching.findall(subrule):
            rule_implicit = True
            adapted_rule = subrule
            while rule_implicit:
                adapted_rule = make_rule_explicit(adapted_rule, rules_dict)

                rule_implicit = any([number_matching.match(part) for part in adapted_rule])
            sub_final_rule.append(adapted_rule)
        if len(sub_final_rule) > 1 and any([True for r in sub_final_rule if '|' in r]):
            # print('simething')
            sub_split = [r.split('|') for r in sub_final_rule]
            sub_final_rule = [''.join(i) for i in product(*sub_split)]

        final_rule.append(sub_final_rule)
    print(final_rule)
    # resolve final rules with more then one "" (double)

    return '|'.join(''.join(line) for line in final_rule)


if __name__ == "__main__":
    print("Welcome to pattern_matching.py")
    rules, messages = split_rules(load_input_file(os.getcwd()))
    print(part_one(rules, messages))
