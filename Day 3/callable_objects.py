#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
def is_even(num):
    return num % 2 == 0

class CallMe:
    def __call__(self):
        print("Called!")





# --------------------------------------------------
def main():
    """Make your noise here"""
    print(callable(is_even))
    #even lambdas are callables
    is_odd = lambda x: x % 2 == 1
    print(callable(is_odd))
    #class are callable
    print(callable(list))
    #methods are callable
    print(callable(list.append))
    #user defined classes
    call_me = CallMe()
    print(callable(call_me))







# --------------------------------------------------
if __name__ == '__main__':
    main()
