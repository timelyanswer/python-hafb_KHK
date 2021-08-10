#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose: review map function
"""

def combine(size, color, anmial):
    return f'{size} {color} {animal}'


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Map() is lazy.  It only produces the values as they are needed
    # ord: unicode value

    m = map(ord, 'The purple Weber State')
    print(m)
    # can print one by one, or on demand
    print(next(m))
    print(next(m))
    print(next(m))
    # print(list(m))

    # or all in one
    print(list(map(ord, 'The purple Weber State')))

    # or use a loop
    for o in map(ord, 'The purple Weber State'):
        print(o)

    # multiple mapping
    sizes = ['small', 'medium', 'large']
    colors = ['green', 'blue', 'red']
    animals = ['dog', 'cat', 'snake']

    # create a list form a map
    # note: do not add the () to combine definition, see above
    print(list(map(combine, sizes, colors, animals)))


    # comprehension
    print([str(i) for i in range(5)])

    print(list(map( str, range (5))))



# --------------------------------------------------
if __name__ == '__main__':
    main()
