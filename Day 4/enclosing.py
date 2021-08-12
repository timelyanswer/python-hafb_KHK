#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: explore when the LEGB rule does not apply
the LEGB rule does not apply when making new bindings
"""

import time

message = 'global'

def make_timer():
    last_call = None
    def elapse():
        nonlocal last_call
        now = time.time()
        if last_call is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return elapse       # no ()



def enclosing():
    message = 'enclosing'
    def local():
        # bring global to scope
        global message          # bring global to scope
        nonlocal message        # bring to scope
        message = 'local'

    print(f'enclosing message {message}')
    local()
    print(f'enclosing message {message}')


# --------------------------------------------------
def main():
    """Make your noise here"""

    # print(f'global message {message}')
    # enclosing()
    # print(f'global message {message}')
    t = make_timer()
    print(t())
    time.sleep(2)
    print(t())
    time.sleep(3)
    print(t())



# --------------------------------------------------
if __name__ == '__main__':
    main()
