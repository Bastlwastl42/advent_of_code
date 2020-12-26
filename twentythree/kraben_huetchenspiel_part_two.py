#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 26/12/2020 13:54

@author: Sebastian

kraben_huetchenspiel_part_two.py is a script for second attempt on day 23 part two
"""
from twentythree.Kraben_Huetchenspiel import get_million_starting_positions
import json


class KrabenHutchenspiel:

    def __init__(self, starting_number):
        # create a dict as double linked list
        self.hutchen_dict = {key: {'prev': -1, 'next': -1} for key in starting_number}
        self.current_cup = starting_number[0]
        self.one = -1
        self.two = -1
        self.three = -1
        self.destination_cup = -1
        self.next_three = [self.one, self.two, self.three]
        max_len = len(starting_number)
        for counter, key in enumerate(self.hutchen_dict.keys()):
            prev = starting_number[counter - 1]
            if counter + 1 == max_len:
                next = starting_number[0]
            else:
                next = starting_number[counter + 1]
            self.hutchen_dict[key] = {'prev': prev, 'next': next, 'current': key}

    def get_next_three(self):
        self.one = self.hutchen_dict[self.hutchen_dict[self.current_cup]['next']]
        self.two = self.hutchen_dict[self.one['next']]
        self.three = self.hutchen_dict[self.two['next']]
        self.next_three = [self.one['current'], self.two['current'], self.three['current']]
        # link the current cup to the next of three
        self.hutchen_dict[self.current_cup]['next'] = \
            self.hutchen_dict[self.three['current']]['next']
        self.hutchen_dict[self.hutchen_dict[self.three['current']]['next']]['prev'] = \
            self.current_cup

    def pick_destination_cup(self):
        self.destination_cup = self.current_cup - 1
        while self.destination_cup in self.next_three or self.destination_cup <= 0:
            self.destination_cup -= 1
            if self.destination_cup <= 0:
                self.destination_cup = max(self.hutchen_dict.keys())

    def insert_next_three_after_destination(self):
        next_to_destination = self.hutchen_dict[self.destination_cup]['next']
        self.hutchen_dict[self.destination_cup]['next'] = self.one['current']
        self.hutchen_dict[self.one['current']]['prev'] = self.destination_cup

        self.hutchen_dict[self.three['current']]['next'] = next_to_destination
        self.hutchen_dict[next_to_destination]['prev'] = self.three['current']

    def shuffle_cups(self, iterations):
        # current cup is considered set
        for counter in range(iterations):
            if counter % (iterations / 100) == 0:
                print(counter)
            # pick the next three cups to the current cup, store in self.next_three
            self.get_next_three()
            # pick destination cup, stored in self.destiantion_cup
            self.pick_destination_cup()
            # keep turning until current cup is on front
            self.insert_next_three_after_destination()
            # update current cup
            self.current_cup = self.hutchen_dict[self.current_cup]['next']

        # return the list starting with one after the 1
        final_list = [self.hutchen_dict[1]['next']]
        counter = final_list[-1]
        while counter != 1:
            final_list.append(self.hutchen_dict[counter]['next'])
            counter = final_list[-1]
        return final_list[:-1]

    def get_part_two(self):
        one = self.get_value_entry(1)
        next_to_one = self.get_value_entry(one['next'])
        return one['next']*next_to_one['next']

    def get_value_entry(self, value):
        return self.hutchen_dict[value]


if __name__ == "__main__":
    print("Welcome to kraben_huetchenspiel_part_two.py")

    starting_string = '562893147'
    million_starting_numbers = get_million_starting_positions(starting_string)
    my_game = KrabenHutchenspiel(million_starting_numbers)
    final_vals = my_game.shuffle_cups(10000000)
    print(my_game.get_part_two())
