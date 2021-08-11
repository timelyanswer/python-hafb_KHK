#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:check your code with assertion
"""

def modulus_four(n):
    r = n % 4
    if r == 0:
        print('Multiple of 4')
    elif r == 1:
        print('remainder 1')
    elif r == 2:
        print('remainder 2')
    elif r == 3:
        print('remainder 3')
    else:   # never case, i.e. never occurs
        assert False, 'this should never happen'






# --------------------------------------------------
def main():
    """Make your noise here"""
    # assert False, 'the condition is false'
    # assert 5 > 2, 'you are in a weird universe'
    modulus_four(4)
    modulus_four(3)





# --------------------------------------------------
if __name__ == '__main__':
    main()
