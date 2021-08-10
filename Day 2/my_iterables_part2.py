#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose: continue comprehension and iterables
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    # list comprehensions: [expr(item) for item in iterable]

    # set comprehensions: {expr(item) for item in iterable}
    s = {i for i in range(10)}
    print(s)
    # dict comprehensions: {key_expr: value_expr for item in iterable}
    d = {i: i * 2 for i in range(10)}
    print(d)

    # comprehensions: (item or item in iterable)
    g = (i for i in range(10))
    print(g)

    # Multiple if-clauses
    # points = []
    # for x in range (5):
    #    for y in range (x):
    #        points.append((x,y))
    # print(points)

    # list comprehension
    points = [(x, y) for x in range(5) for y in range(5)]
    print(points)

    # version 1: loops
    values = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x - y != 0:
                    values.append(x / (x - y))
    print(values)


# --------------------------------------------------
if __name__ == '__main__':
    main()
