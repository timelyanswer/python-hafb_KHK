#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose:continue discussion on arguments
"""

def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):

    """

    print argument info
    arg1: first required position argument
    arg2: second required position argument
    args: optional list of positional arguments
    kwarg1: first keyword argument
    kwarg2: second keyword argument
    kwargs: optional list of keyword argument
    """

    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)

def print_pos_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

def colors(red, blue, green, **kwargs):
    print(f'r={red}')
    print(f'b={blue}')
    print(f'g={green}')
    print(kwargs)



# --------------------------------------------------
def main():
    """Make your noise here"""
    print_args(1, 2, kwarg1='hello', kwarg2='there')    # minimum to run
    print_args(1, 2, 3, 4, kwarg1='hello', kwarg2='there')  # two optional positional params
    print_args(1, 2, 4, 4,
               kwarg1='hello', kwarg2='there',
               fname='Waldo', lname='Weber')    # two optional positional and keyword params

    t = (11, 22, 33, 44, 55, 66)
    print_pos_args(*t)
    print_pos_args(t[0], t[1], t[2:])   # prints first, second, and the rest of the positions

    # defining the dictionary
    k = {'red': 21, 'blue':120, 'green':68, 'alpha':52}
    colors(**k)














# --------------------------------------------------
if __name__ == '__main__':
    main()
