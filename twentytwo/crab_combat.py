#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 22/12/2020 10:58

@author: Sebastian

crab_combat.py is a script for advent of code day 22
"""

import os
from copy import deepcopy
from typing import List

from common import load_input_file


def play_crab_combat(player_one: List[int], player_two: List[int]) -> List[int]:
    while len(player_one) * len(player_two):
        pone_card = player_one.pop(0)
        ptwo_card = player_two.pop(0)
        if pone_card > ptwo_card:
            player_one.append(pone_card)
            player_one.append(ptwo_card)
        else:
            player_two.append(ptwo_card)
            player_two.append(pone_card)
    if len(player_one):
        return player_one
    return player_two


def play_recursive_crab_combat(player_one: List[int], player_two: List[int]) -> (List[int], bool):
    previously_played_decks_pone = []
    previously_played_decks_ptwo = []
    while len(player_one) * len(player_two):
        # check previous rounds
        check_prev_game_pone = deepcopy(player_one)
        check_prev_game_ptwo = deepcopy(player_two)
        if check_prev_game_pone in previously_played_decks_pone or \
                check_prev_game_ptwo in previously_played_decks_ptwo:
            print('Finish game by recursive rule!')
            return player_one, True
        previously_played_decks_pone.append(check_prev_game_pone)
        previously_played_decks_ptwo.append(check_prev_game_ptwo)
        pone_card = player_one.pop(0)
        ptwo_card = player_two.pop(0)
        if len(player_one) >= pone_card and len(player_two) >= ptwo_card:
            new_player_one = deepcopy(player_one[:pone_card])
            new_player_two = deepcopy(player_two[:ptwo_card])
            winner, player_one_wins = play_recursive_crab_combat(new_player_one, new_player_two)
            if player_one_wins:
                print('\t\tPlayer one wins subgame!')
                player_one.append(pone_card)
                player_one.append(ptwo_card)
            else:
                print('\t\tPlayer two wins subgame!')
                player_two.append(ptwo_card)
                player_two.append(pone_card)
            continue
        # if no subgame, play normal round
        if pone_card > ptwo_card:
            print('\tPlayer one wins round!')
            player_one.append(pone_card)
            player_one.append(ptwo_card)
        else:
            print('\tPlayer two wins round!')
            player_two.append(ptwo_card)
            player_two.append(pone_card)
    if len(player_one):
        print('Player one wins game!')
        return player_one, True
    print('Player two wins game!')
    return player_two, False


def get_score(winning_deck: List[int]) -> int:
    return sum([(counter + 1) * value for counter, value in enumerate(reversed(winning_deck))])


def deal_hands(input_lines: List[str]) -> (List[int], List[int]):
    for counter, value in enumerate(input_lines):
        if value != '':
            continue
        player_one = [int(val) for val in input_lines[1:counter]]
        player_two = [int(val) for val in input_lines[counter + 2:]]
        return player_one, player_two


if __name__ == "__main__":
    print("Welcome to crab_combat.py")
    player_one, player_two = deal_hands(load_input_file(os.getcwd()))
    winning_deck = play_crab_combat(player_one, player_two)
    print(get_score(winning_deck))
    player_one, player_two = deal_hands(load_input_file(os.getcwd()))
    winning_deck_part_two, player_one_won = play_recursive_crab_combat(player_one, player_two)
    print(player_one_won)
    print(get_score(winning_deck_part_two))
