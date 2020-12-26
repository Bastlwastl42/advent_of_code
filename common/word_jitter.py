#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 25/12/2020 18:48

@author: Sebastian Lehrack

word_jitter.py is a script for....
"""
from itertools import permutations

import duden

if __name__ == "__main__":
    print("Welcome to word_jitter.py")
    letters = ['a', 'e', 't', 'i', 'p', 's', 'r']

    for word in permutations(letters):
        da_word = f'{word[0].capitalize()}{word[1]}{word[2]}{word[3]}{word[4]}{word[5]}{word[6]}'
        print(da_word)
        w = duden.search(da_word)
        if w:
            print('found!!:')
            print(w)
            break


