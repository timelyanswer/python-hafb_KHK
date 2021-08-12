#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: function that returns functions
"""

def enclosing():
    x = 'close over'
    def local_func():
        print(x)
    return local_func   # without parenthesis means you're invoking it

def test_enclosing():
    lf = enclosing()
    lf()
    print(lf.__closure__)





# --------------------------------------------------
def main():
    """Make your noise here"""
    test_enclosing()




# --------------------------------------------------
if __name__ == '__main__':
    main()
