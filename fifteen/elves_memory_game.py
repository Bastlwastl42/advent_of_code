#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 15/12/2020 07:55

@author: Sebastian Lehrack

elves_memory_game.py is a script for advent of code day 15
"""
from typing import List


def gimme_number_twenty_twenty(starting_numbers: List[int], last_pos):
    numbers_spoken_full_sequence = starting_numbers
    numbers_spoken_look_up_dict = {}
    # initial setup
    for counter, val in enumerate(numbers_spoken_full_sequence):
        numbers_spoken_look_up_dict[val] = [counter + 1]

    spoken_numbers = len(numbers_spoken_full_sequence)
    while spoken_numbers < last_pos:
        if spoken_numbers % 100000 == 0:
            print(f'passing {spoken_numbers}')
        last_number = numbers_spoken_full_sequence[-1]
        if last_number in numbers_spoken_look_up_dict.keys():
            # get the difference and add this value
            # the counter is zero index!
            if len(numbers_spoken_look_up_dict[last_number]) == 1:
                last_spoken = numbers_spoken_look_up_dict[last_number][-1]
            else:
                last_spoken = numbers_spoken_look_up_dict[last_number][-2]
            new_append = len(numbers_spoken_full_sequence) - last_spoken
            numbers_spoken_full_sequence.append(new_append)
            # numbers_spoken_look_up_dict[last_number] = len(numbers_spoken_full_sequence)
            if new_append in numbers_spoken_look_up_dict.keys():
                numbers_spoken_look_up_dict[numbers_spoken_full_sequence[-1]].append(
                    len(numbers_spoken_full_sequence))
            else:
                numbers_spoken_look_up_dict[new_append] = [len(numbers_spoken_full_sequence)]
        else:
            numbers_spoken_full_sequence.append(0)
        spoken_numbers += 1
    return numbers_spoken_full_sequence[-1]


if __name__ == "__main__":
    print("Welcome to elves_memory_game.py")

    puzzle_input = [int(i) for i in '0,13,1,8,6,15'.split(',')]
    print('Part 1')
    print(gimme_number_twenty_twenty(puzzle_input, 2020))
    print('Part 2')
    print(gimme_number_twenty_twenty(puzzle_input, 30000000))
