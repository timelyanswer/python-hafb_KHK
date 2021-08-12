#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose:forward arguments
"""

from pprint import pp


def trace(f, *args, **kwargs):
    print(f'args={args}')
    print(f'kwargs={kwargs}')
    result = f(*args, **kwargs)
    print(f'result{result}')
    return result


def test_trace():
    print(int("ff", base=16))
    trace(int, "ff", base=16)

def test_tables():
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 22, 24, 28, 22, 20, 18, 22]
    daily = [sunday, monday, tuesday]
    pp(daily)

    # print(*sunday) - it will print the entire

    # for item in zip(sunday, monday, tuesday):
    for item in zip(*daily):
        print(item)

    transposed = list(zip(*daily))
    pp(transposed)









# --------------------------------------------------
def main():
    """Make your noise here"""
    test_trace()




# --------------------------------------------------
if __name__ == '__main__':
    main()
