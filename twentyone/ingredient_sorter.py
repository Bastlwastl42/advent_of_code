#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 21/12/2020 09:43

@author: Sebastian

ingredient_sorter.py is a script for advent of code day 21
"""

import os

from common import load_input_file


def create_ingredient_dict(input_lines):
    ingredient_dict = {}
    ing_list = []
    for ingredients, allergies in input_lines:
        ing_split = ingredients.rstrip().split(' ')
        all_split = allergies.split(', ')
        # remove last )
        all_split[-1] = all_split[-1][:-1]
        # create a list of allergen possible in these ingredients
        # cross of one by one
        # each allergen is in exactly one ingredient!
        ing_list.extend(ing_split)
        for allergen in all_split:
            if allergen in ingredient_dict.keys():
                # check of ing newly given
                ingredient_dict[allergen] = [i for i in ing_split if i in ingredient_dict[allergen]]
            else:
                # create a new entry, provifing all current ingredients
                ingredient_dict[allergen] = ing_split
    # filter ingredient dict by clear hits: only one item left
    max_leng = len(ingredient_dict)
    new_ing_dict = {}
    while len(new_ing_dict) < max_leng:
        # ingredient_dict = {key: val for key, val in ingredient_dict if len(val) > 0}
        for allergen, ingredients in ingredient_dict.items():
            if not len(ingredients) == 1:
                continue
            [current_ing] = ingredient_dict.get(allergen)
            new_ing_dict[allergen] = current_ing
            for key in ingredient_dict.keys():
                try:
                    ingredient_dict[key].remove(current_ing)
                except ValueError:
                    continue
            break
    return new_ing_dict, ing_list

def part_one(input_lines):
    ingredient_dict, ing_list = create_ingredient_dict(input_lines)
    return len([ing for ing in ing_list if ing not in ingredient_dict.values()])

def part_two(input_lines):
    ingredient_dict, ing_list = create_ingredient_dict(input_lines)
    #sort alphabetically by allergen
    sorted_allergies = sorted(ingredient_dict.keys())
    return ','.join([ingredient_dict[key] for key in sorted_allergies])


if __name__ == "__main__":
    print("Welcome to ingredient_sorter.py")
    input_lines = [line.split('(contains ') for line in
                   load_input_file(os.getcwd())]

    print(part_one(input_lines))
    print(part_two(input_lines))
