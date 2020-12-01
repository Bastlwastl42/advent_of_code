#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 01/12/2020 08:56

@author: Sebastian Lehrack

get_multiple_of_2020.py is a script for advent of code 01/01
"""
import os
import copy
FIXED_MULTIPLE = 2020

if __name__ == "__main__":
    print("Welcome to get_multiple_of_2020.py")
    code_input = os.path.join(os.getcwd(), 'input.txt')
    with open(code_input, 'r') as f:
        input_list = [int(element) for element in f.readlines()]
    print(len(input_list))
    remainder_list = copy.copy(input_list)
    for number in input_list:
        rest = FIXED_MULTIPLE-number
        if rest < 0 or rest not in remainder_list:
            remainder_list.remove(number)
            continue
        print(f'Found sum of 2020 with {number} and {rest}')
        print(f'Multiple is {number*rest}')
        break

    break_flag = False
    for number in input_list:
        for sec_number in [e for e in input_list if not e == number]:
            if number+sec_number > FIXED_MULTIPLE:
                continue
            for third_number in [t for t in input_list if not t in [number, sec_number]]:
                if number+sec_number+third_number == FIXED_MULTIPLE:
                    print(f'found {number}, {sec_number}, {third_number}')
                    print(f'Checksum {number+sec_number+third_number}')
                    print(f'Checkfactor {number*sec_number*third_number}')
                    break_flag = True
                    break
            if break_flag:
                break
        if break_flag:
            break

    #print(input_list)


