#!/usr/bin/env python3

"""a dice roll program
"""

import colors as c
import time
import random

def roll(howmany=1,sides=6):
    """Returns the result from rolling 'hawmany' of 'sides'-sides dice"""
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
    return total

def parse(text):
    """Parses traditional dice notation (ex: 3d6)"""
    howmany, sides = text.split('d')
    return (int(howmany), int(sides))

def parse_roll(text):
    """Parses traditional dice notation and then rolls (ex: 3d6)"""
    howmany, sides = text.split('d')
    return (int(howmany), int(sides))

if __name__ == '__main__':
    while True:
        print(c.clear)
        print(roll())
        time.sleep(0.5)
