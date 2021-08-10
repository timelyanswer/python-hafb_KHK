#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------

def main():
    """Make your noise here"""
    r = [4, -2, 10, -18, 22, 55, 2, 77]
    # Slicing
    print(r[2:6])
    print(f'len of linst {len(r)} ')
    print(f'last element {r[-1]} ')
    #Copy list, by default Python uses Shallow copies
    t = r
    print(f'1) is t the same as r? {t is r}')
    # to make a copy, generate a new list
    u = r[:]
    print(f'2) is u the same as r? {u is r}')
    v = r.copy()_# faster
    print(f'2) is v the same as r? {v is r}')
    print(f'2) is v the equivalent as r? {v == r}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
