#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

def fibo():
    """Fibo series"""
    numbers=[]
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1] #runs one time, because it stops at yield
        continue



def gen246():
    print('about to yield 2')
    yield 2
    print('about to yield 4')
    yield 4
    print('about to yield 6')
    yield 6
    print('about to return')

def gen123():
    yield 1
    yield 2
    yield 3


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('Iterable is empty')

# --------------------------------------------------

def main():
    """Review iterator and generators"""
    #iterable = ['spring', 'summer', 'fall', 'winter']
    #print(first(iterable))
    #print(first(iterable))
    g = gen123()
    #print(type(g))
    for v in gen123():
        print(f'value is {v}')




# --------------------------------------------------
if __name__ == '__main__':
    main()
