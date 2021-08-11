#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

def hyper_volume(length, *lengths):
    # print(lengths)
    # print(type(lengths))
    #i = iter(lengths)
    # v = next(i)
    #for length in i:
    i = iter(lengths)
    v = lengths
    for item in i:
        v *= length
    return v

def tag(name, **attributes):
    """arbitrary number of keyword
    arguments use the ** symbol"""

    # print(name)
    # print(attributes)
    # print(type(attributes))
    result = '<' + name
    # task add info from attributes

    for key, value in attributes.items():
        result += f'{key}="{str(value)}",'
    result += '>'
    return result




# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(hyper_volume(3, 4))
    # print(hyper_volume(3, 4, 5, 6))
    # print(hyper_volume(3))
    # print(hyper_volume())
    # tag('img')
    tag('img', src='monet.jpg',
    alt='somewhere in europe', border=1)






# --------------------------------------------------
if __name__ == '__main__':
    main()
