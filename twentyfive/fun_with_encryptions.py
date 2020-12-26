#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 26/12/2020 12:53

@author: Sebastian

fun_with_encryptions.py is a script for advent of code day 25
"""
import os

from common import load_input_file

subject_number = lambda x, s: (x * s) % 20201227
subject_base = 7


def get_loop_number(public_key: int) -> int:
    # these value are better cached, if possible
    loop_counter = 1
    counter = 7
    while counter != public_key:
        counter = subject_number(counter, subject_base)
        loop_counter += 1
    return loop_counter


def get_encryption_key(public_key: int, loop_number: int) -> int:
    encryption_key = public_key
    # key_list = [public_key]
    for counter in range(1, loop_number):
        encryption_key = subject_number(encryption_key, public_key)
        # key_list.append(encryption_key)
    return encryption_key


if __name__ == "__main__":
    print("Welcome to fun_with_encryptions.py")
    public_keys = [int(i) for i in load_input_file(os.getcwd())]

    door_public = public_keys[0]
    card_public = public_keys[1]

    door_loop_number = get_loop_number(door_public)
    card_loop_number = get_loop_number(card_public)

    encryption_door = get_encryption_key(door_public, card_loop_number)
    encryption_card = get_encryption_key(card_public, door_loop_number)

    if encryption_card == encryption_door:
        print(f'encryption succeeded! {encryption_door}')
    else:
        print(f'failure during encryption: {encryption_door} {encryption_card}')
