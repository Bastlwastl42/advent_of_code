#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 23/12/2020 19:59

@author: Sebastian

Kraben_Huetchenspiel.py is a script for advent fo code day 23
"""

import collections
from typing import List


# rotate(-1) is a left shift (pushing numbers to the left)

def shufle_cups(starting_numbers: List[int], number_of_turns: int = 100):
    current_cup = starting_numbers[0]
    current_numbers = collections.deque(starting_numbers)
    for counter in range(number_of_turns):
        if counter % 100000 == 0:
            print(counter)
        # pick the next three cups to the current cup
        next_three, remainder = pick_next_three(current_numbers, current_cup)
        # pick destination cup from remainder
        destination_cup = pick_destination_cup(remainder, current_cup)
        current_numbers = remainder[0:destination_cup + 1]
        current_numbers.extend(next_three)
        current_numbers.extend(remainder[destination_cup + 1:])
        # keep turning until current cup is on front
        current_numbers = collections.deque(current_numbers)
        while current_numbers[-1] != current_cup:
            current_numbers.rotate(-1)
        current_cup = current_numbers[0]

    # return the list starting with one after the 1
    while current_numbers[-1] != 1:
        current_numbers.rotate(-1)
    return list(current_numbers)[:-1]


def pick_next_three(list_of_numbers, current_cup):
    # resort so current cup is in front
    act_list = list_of_numbers
    while act_list[-1] != current_cup:
        act_list.rotate(-1)
    return list(act_list)[0:3], list(act_list)[3:]


def pick_destination_cup(remainder, current_cup_label):
    label_search_counter = current_cup_label - 1
    while True:
        if label_search_counter not in remainder:
            label_search_counter -= 1
            if label_search_counter < 1:
                label_search_counter = max(remainder)
            continue
        return remainder.index(label_search_counter)


def get_starting_positions(input_line: str):
    return [int(i) for i in input_line]


def get_million_starting_positions(input_line: str):
    starting_numbers = [int(i) for i in input_line]
    starting_numbers.extend(range(max(starting_numbers) + 1, 1000000))
    return starting_numbers


if __name__ == "__main__":
    print("Welcome to Kraben_Huetchenspiel.py")
    starting_string = '562893147'
    starting_numbers = get_starting_positions(starting_string)
    # print(shufle_cups(starting_numbers))
    for i in shufle_cups(starting_numbers):
        print(i, end='')
    print('\n')

    million_starting_numbers = get_million_starting_positions(starting_string)
    final_values = shufle_cups(million_starting_numbers, 10000000)
    print(final_values[-1] * final_values[0])
