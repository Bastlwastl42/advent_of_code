#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 16/12/2020 08:41

@author: Sebastian

train_ticket_checker.py is a script for advent of code day 16
"""
import os
import math
from typing import Set, List

from common import load_input_file


def get_valid_numbers(rules: List[str]):
    all_rules = [rule_tuple for rule_list in get_rule_dict(rules).values() for rule_tuple in
                 rule_list]
    return set([j for low, high in all_rules for j in range(low, high + 1)])


def get_rule_dict(rules: List[str]):
    rule_dict = {}
    for rule_name, rule_value in [i.split(': ') for i in rules]:
        single_rule_values = [i.split('-') for i in rule_value.split(' or ')]

        rule_dict[rule_name] = [(int(i[0]), int(i[1])) for i in single_rule_values]
    return rule_dict


def ticket_is_valid(valid_numbers: Set[int], ticket_numbers: List[str]) -> bool:
    return all([int(i) in valid_numbers for i in ticket_numbers])


def get_input_fields(input_lines: List[str]):
    split_lines = [counter for counter, val in enumerate(input_lines) if val == '']
    rules = input_lines[0:split_lines[0]]
    [my_ticket] = [line.split(',') for line in input_lines[split_lines[1] - 1:split_lines[1]]]
    nearby_tickets = [line.split(',') for line in input_lines[split_lines[1] + 2:]]
    return rules, my_ticket, nearby_tickets


def check_error_codes(input_lines: List[str]) -> int:
    rules, _, nearby_tickets = get_input_fields(input_lines)
    # setup rules
    invalid_numbers = []
    valid_numbers = get_valid_numbers(rules)
    for field_numbers in nearby_tickets:
        for field_num in [int(i) for i in field_numbers]:
            if field_num in valid_numbers:
                continue
            else:
                invalid_numbers.append(field_num)

    return sum(invalid_numbers)


def match_rule(rule, value) -> bool:
    return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]


if __name__ == "__main__":
    print("Welcome to train_ticket_checker.py")
    # part one
    print(check_error_codes(load_input_file(os.getcwd())))

    # part two
    rules, my_ticket, nearby_tickets = get_input_fields(load_input_file(os.getcwd()))
    valid_numbers = get_valid_numbers(rules)
    rules_dict = get_rule_dict(rules)
    valid_tickets = [ticket for ticket in nearby_tickets if ticket_is_valid(valid_numbers, ticket)]

    # initialize possible fields
    valid_fields = {i: [key for key in rules_dict.keys()] for i in range(len(my_ticket))}

    # consider all tickets valid
    for ticket in valid_tickets:
        for field, value in enumerate(ticket):
            for possible_rule in valid_fields[field]:
                if not match_rule(rules_dict[possible_rule], int(value)):
                    try:
                        valid_fields[field].remove(possible_rule)
                    except ValueError:
                        continue
    final_fields = {}
    max_length = len(valid_fields)
    while len(final_fields) < max_length:
        print(f'currently have {len(final_fields)} final values identified')
        for index, possible_field in valid_fields.items():
            if len(possible_field) > 1:
                continue
            # if value is equal to one, remove this from all other possibilities and repeat search
            [single_el] = valid_fields.pop(index)
            final_fields.update({index: single_el})
            for rem_index in valid_fields.keys():
                valid_fields[rem_index].remove(single_el)
            break

    # identify the values on my ticket
    my_final_ticket = {name: my_ticket[index] for index, name in final_fields.items()}
    print(f'The product of departure value is {math.prod([int(value) for name, value in my_final_ticket.items() if name.startswith("departure")])}')
