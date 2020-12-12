#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on 12/12/2020 09:24

@author: Sebastian

ships_movements.py is a script for advent of code 12
"""
import math
import os

from common import load_input_file

# direction encoding: north: 0

DIRECTIONS_DICT = {'north': 0, 'east': 1, 'south': 2, 'west': 3}


class Vector:
    """a 2dimensional vektor class"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return self.a * other.b + self.b * other.b

    def skalar_mult(self, skalar):
        return Vector(self.a * skalar, self.b * skalar)

    def cross_product(self, other):
        pass

    def __abs__(self):
        return round(math.sqrt(self.a * self.a + self.b * self.b))

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f'({self.a}, {self.b})'


class RotMatrix:
    """a 2dimensional rotation matrix class"""

    def __init__(self, degrees: int, direction: str):
        """
        (a=cos x    b=-sin x)
        (c=sin x    d=cos x)
        Rotation is counterclock-wise i.e left. Rotation to right is convert by
        planear symmetric angles. I.e. r90 == l270
        """
        if direction == 'R':
            self.degrees = math.radians(360 - degrees)
        else:
            self.degrees = math.radians(degrees)
        self.a = round(math.cos(self.degrees))
        self.b = round(-1 * math.sin(self.degrees))
        self.c = round(math.sin(self.degrees))
        self.d = round(math.cos(self.degrees))

    def rotate(self, vector: Vector):
        return Vector(self.a * vector.a + self.b * vector.b, self.c * vector.a + self.d * vector.b)


HIMMELSRICHTUNG_VECTORS = {'N': Vector(0, 1), 'E': Vector(1, 0), 'S': Vector(0, -1),
                           'W': Vector(-1, 0)}
ROTATIONS_VEKTOR = {'L': (-1, 1), 'R': (1, -1)}


class Ship:

    def __init__(self):
        # face east in the beginning
        self.face = HIMMELSRICHTUNG_VECTORS['E']
        self.position = Vector(0, 0)

    def take_command(self, command, distance):
        """Switch case for command"""
        if command in ['N', 'E', 'S', 'W']:
            self.move_ship_himmelsrichtung(command, distance)
        if command in ['L', 'R']:
            self.turn_ship(command, distance)
        if command in ['F']:
            self.move_forward(distance)

    def move_ship_himmelsrichtung(self, command: str, distance: int):
        """Move the ship in the given Himmelsrichtung without turning"""
        self.position += HIMMELSRICHTUNG_VECTORS[command].skalar_mult(distance)

    def move_forward(self, distance: int):
        """Take self.face and add to position"""
        self.position += self.face.skalar_mult(distance)

    def turn_ship(self, direction: str, degrees: int):
        """take rotation and adapt self.face"""
        self.face = RotMatrix(degrees, direction).rotate(self.face)

    def __str__(self):
        """Printout"""
        return f'Current Position is {self.position} faceing {self.face}.\n' \
            f'Manhattan distance is {abs(self.position.a) + abs(self.position.b)}'


class WaypointShip():
    """A ship coordinated by a waypoint"""

    def __init__(self):
        self.waypoint = Vector(10, 1)
        self.position = Vector(0, 0)

    def take_command(self, command, distance):
        """Switch case for command"""
        if command in ['N', 'E', 'S', 'W']:
            self.adapt_waypoint(command, distance)
        if command in ['L', 'R']:
            self.rotate_waypoint(command, distance)
        if command in ['F']:
            self.move_forward(distance)

    def adapt_waypoint(self, command, distance):
        """add to the given waypoint"""
        self.waypoint += HIMMELSRICHTUNG_VECTORS[command].skalar_mult(distance)

    def rotate_waypoint(self, direction: str, degrees: int):
        self.waypoint = RotMatrix(degrees, direction).rotate(self.waypoint)

    def move_forward(self, distance: int):
        """move distance times distance to waypoint"""
        self.position += self.waypoint.skalar_mult(distance)

    def __str__(self):
        """Printout"""
        return f'Current Position is {self.position} waypoint at  {self.waypoint}.\n' \
            f'Manhattan distance is {abs(self.position.a) + abs(self.position.b)}'


if __name__ == "__main__":
    print("Welcome to ships_movements.py")
    input_lines = load_input_file(os.getcwd())
    # part one
    my_ship = Ship()
    # part two
    my_waypoint_ship = WaypointShip()
    for line in input_lines:
        command = line[0]
        distance = int(line[1:])
        my_ship.take_command(command, distance)
        my_waypoint_ship.take_command(command, distance)
        print(my_waypoint_ship)

    print(f'Part one:\n\t{my_ship}\n'
          f'Part two:\n\t{my_waypoint_ship}')
