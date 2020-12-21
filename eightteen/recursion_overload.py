#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 20/12/2020 16:11

@author: Sebastian

recursion_overload.py is a script for advent of code day 18
I heard u like recursions!
"""
import os

from common import load_input_file

MULT = '*'
ADD = '+'


def eval_atom(first, second, operator):
    return eval(f'{first} {operator} {second}')


def straight_eval(line):
    """assume a cleaned list of operations with () or changing sign"""
    if len(line) == 3:
        return eval_atom(line[0], line[2], line[1])
    else:
        return eval_atom(line[0], straight_eval(line[2:]), line[1])


def evaluate_expression(line):
    if len(line) == 3:
        return eval_atom(first=int(line[0][-1]), second=int(line[2][0]), operator=line[1])
    counter_vals = iter(range(len(line) - 1, 0, -2))
    while True:
        counter = next(counter_vals, 0)
        first_el = line[counter]
        if first_el.endswith(')'):
            # resolve term in parenthesis first
            # search closing part, remove parenthesis and return to evalutate_expression
            opening_parathensis = sum([1 for i in first_el if i == ')'])
            el_counter = counter
            while opening_parathensis > 0:
                el_counter = next(counter_vals, 0)
                opening_parathensis += sum([1 for i in line[el_counter] if i == ')']) - sum(
                    [1 for i in line[el_counter] if i == '('])
            last_el = line[el_counter][1:]
            new_line = [last_el]
            new_line.extend(line[el_counter + 1:counter])
            new_line.append(first_el[:-1])
            if el_counter == 0:
                return evaluate_expression(new_line)
            else:
                first_el = evaluate_expression(new_line)
                operator = line[el_counter - 1]
                counter = next(counter_vals, 0)
                if counter == 0:
                    return eval_atom(first_el, line[counter], operator)
                next_el = evaluate_expression(line[0:el_counter - 1])
                return eval_atom(first_el, next_el, operator)
        else:
            first_el = int(line[counter])
            operator = line[counter - 1]
            next_el = evaluate_expression(line[0:counter - 1])
            # print(eval_atom(first_el, next_el, operator))
            return eval_atom(first_el, next_el, operator)


def evaluate_expression_part_two(line):
    if len(line) == 3:
        return eval_atom(first=int(line[0][-1]), second=int(line[2][0]), operator=line[1])
    if len(line) == 1:
        return int(line[0])
    counter_vals = iter(range(len(line) - 1, 0, -2))
    while True:
        counter = next(counter_vals, 0)
        first_el = line[counter]
        if first_el.endswith(')'):
            # resolve term in parenthesis first
            # search closing part, remove parenthesis and return to evalutate_expression
            opening_parathensis = sum([1 for i in first_el if i == ')'])
            el_counter = counter
            while opening_parathensis > 0:
                el_counter = next(counter_vals, 0)
                opening_parathensis += sum([1 for i in line[el_counter] if i == ')']) - sum(
                    [1 for i in line[el_counter] if i == '('])
            last_el = line[el_counter][1:]
            new_line = [last_el]
            new_line.extend(line[el_counter + 1:counter])
            new_line.append(first_el[:-1])
            if el_counter == 0:
                return evaluate_expression_part_two(new_line)
            else:
                first_el = evaluate_expression_part_two(new_line)
                counter = next(counter_vals, 0)
                if counter == 0:
                    return eval_atom(first_el, line[0], line[1])
                operator = line[counter+1]
                while operator == ADD:
                    if line[counter].endswith(')'):
                        opening_parathensis = sum([1 for i in line[counter] if i == ')'])
                        el_counter = counter
                        while opening_parathensis > 0 and el_counter > 0:
                            el_counter = next(counter_vals, 0)
                            opening_parathensis += sum(
                                [1 for i in line[el_counter] if i == ')']) - sum(
                                [1 for i in line[el_counter] if i == '('])
                        last_el = line[el_counter][1:]
                        new_line = [last_el]
                        new_line.extend(line[el_counter + 1:counter])
                        new_line.append(line[counter][:-1])
                        next_el = evaluate_expression_part_two(new_line)
                        if el_counter == 0:
                            return eval_atom(first_el, next_el, operator)
                        first_el = eval_atom(first_el, next_el, operator)
                    else:
                        first_el = eval_atom(first_el, line[counter], line[counter+1])
                    counter = next(counter_vals, 0)
                    if counter == 0:
                        return eval_atom(first_el, line[counter], line[counter + 1])
                    operator = line[counter+1]
                next_el = evaluate_expression_part_two(line[:counter+1])
                return eval_atom(first_el, next_el, operator)
        # carefull here, do add operations first
        operator = line[counter - 1]
        while operator == ADD:
            if line[counter-2].endswith(')'):
                opening_parathensis = sum([1 for i in line[counter-2] if i == ')'])
                el_counter = next(counter_vals, 0)
                while opening_parathensis > 0 and el_counter > 0:
                    el_counter = next(counter_vals, 0)
                    opening_parathensis += sum(
                        [1 for i in line[el_counter] if i == ')']) - sum(
                        [1 for i in line[el_counter] if i == '('])
                last_el = line[el_counter][1:]
                new_line = [last_el]
                new_line.extend(line[el_counter + 1:counter])
                new_line.append(line[counter][:-1])
                next_el = evaluate_expression_part_two(new_line)
                if el_counter == 0:
                    return eval_atom(first_el, next_el, operator)
                first_el = eval_atom(first_el, next_el, operator)
            first_el = eval_atom(first_el, line[counter - 2], operator)
            counter = next(counter_vals, 0)
            if counter == 0:
                return eval_atom(first_el, line[counter], line[counter + 1])
            operator = line[counter - 1]
        next_el = evaluate_expression_part_two(line[0:counter - 1])
        return eval_atom(first_el, next_el, operator)


if __name__ == "__main__":
    print("Welcome to recursion_overload.py")
    input_lines = [line.split(' ') for line in load_input_file(os.getcwd())]

    print(sum([evaluate_expression(line) for line in input_lines]))

    print(sum([evaluate_expression_part_two(line) for line in input_lines]))
