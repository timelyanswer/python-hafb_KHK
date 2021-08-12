#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: class as decorators
"""


class DecoratedClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

@DecoratedClass
def display():
    print('display ran')

@DecoratedClass
def display_info(name, age):
    print(f'display function ran for {name}{age}')

# --------------------------------------------------
def main():
    """Make your noise here"""
    display()
    display_info('waldo', 21)




# --------------------------------------------------
if __name__ == '__main__':
    main()
