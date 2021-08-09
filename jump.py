#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text')

    return parser.parse_args()



# --------------------------------------------------
def main():
    """encode phone number using the jumper five algorithm"""

    args = get_args()
    jumper ={'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6':
             '4', '7': '3', '8': '2', '9': '1', '0': '5'}


    # Method #1
    for char in args.text:
        print(jumper.get(char, char), end='')
    print()

    #Method #2
    for char in args.text:
        new_text += jumper.get(char, char)
        print(new_text)

    #Method #3
    new_text = []
        for char in args.text:
        new_text.append(jumper.get(char, char))
        print(' '.join(new_text))

    #Method #4
    print(''.join([jumper.get(char, char) for char in args.text]))

    #Method #5


# --------------------------------------------------
