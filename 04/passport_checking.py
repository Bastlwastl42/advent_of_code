#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 04/12/2020 08:48

@author: Sebastian

passport_checking.py is a script for advent of code part 04

"""
import os
from common import load_input_file
from typing import List
import re

"""hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76."""
height_re = re.compile('\d(cm)?(in)?')

"""hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
hcl_re = re.compile('#[0-9a-f]{6,6}')

pid_re = re.compile('\d{9,9}')

four_digit_checks = re.compile('\d{4,4}')


class Passport():

    def __init__(self, input_line):
        self.passport_vals = {key: val for (key, val) in [e.split(':') for e in line]}

    def is_valid(self):
        """Checks if all required fields are given
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)
        """
        list_of_req_keys = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        list_of_optional_keys = ['cid']
        list_of_given_keys = sorted(self.passport_vals.keys())
        if list_of_req_keys == list_of_given_keys or sorted(
                list_of_req_keys + list_of_optional_keys) == list_of_given_keys:
            return True
        return False

    def check_all(self):
        """Check all valuess"""
        return_val = all([self.check_byr(), self.check_cid(),
                          self.check_ecl(), self.check_eyr(),
                          self.check_hcl(), self.check_hgt(),
                          self.check_iyr(), self.check_pid()])
        return return_val

    def check_byr(self) -> bool:
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        if four_digit_checks.match(self.passport_vals['byr']):
            return 1920 <= int(self.passport_vals['byr']) <= 2002
        return False

    def check_iyr(self) -> bool:
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        if four_digit_checks.match(self.passport_vals['iyr']):
            return 2010 <= int(self.passport_vals['iyr']) <= 2020
        return False

    def check_eyr(self) -> bool:
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        if four_digit_checks.match(self.passport_vals['eyr']):
            return 2020 <= int(self.passport_vals['eyr']) <= 2030
        return False

    def check_hgt(self) -> bool:
        """hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76."""
        matched_height = height_re.match(self.passport_vals['hgt'])
        if matched_height:
            # print(f'ding: {matched_height.string}')

            if matched_height.string[-1] == 'm':
                try:
                    if len(matched_height.string) != 5:
                        # print('False')
                        return False
                    # print(f'{int(matched_height.string[0:3])} is {150 <= int(matched_height.string[0:3]) <= 193}')
                    return 150 <= int(matched_height.string[0:3]) <= 193
                except ValueError:
                    # print('False')
                    return False
            if len(matched_height.string) != 4:
                # print('False')
                return False
            # print(f'{int(matched_height.string[0:2])} is {59 <= int(matched_height.string[0:2]) <= 76}')
            return 59 <= int(matched_height.string[0:2]) <= 76
        return False

    def check_hcl(self) -> bool:
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        if hcl_re.match(self.passport_vals['hcl']):
            return True
        return False

    def check_ecl(self) -> bool:
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        return self.passport_vals['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self) -> bool:
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        if pid_re.match(self.passport_vals['pid']):
            return True
        return False

    def check_cid(self) -> bool:
        """cid (Country ID) - ignored, missing or not."""
        return True


if __name__ == "__main__":
    print("Welcome to passport_checking.py")
    flat_split_input = '\n'.join(load_input_file(os.getcwd())).split('\n\n')
    list_of_valid_passports: List[Passport] = []
    for line in flat_split_input:
        line = line.replace('\n', ' ').split(' ')
        if len(line) not in [7, 8]:
            continue
        act_passport = Passport(input_line=line)
        if act_passport.is_valid():
            list_of_valid_passports.append(act_passport)

    print(f'Found {sum([1 for e in list_of_valid_passports if e.is_valid()])} valid Passports by '
          f'simple field check')

    print(
        f'Rechecking values found {sum([1 for e in list_of_valid_passports if e.check_all() and e.is_valid()])} valid Passports.')
