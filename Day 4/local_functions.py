#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose:learn how local functions work
"""
def func1():
    """regular function"""
    x=1
    y=2
    return x+y

def func2():
    """regular function"""
    def local_func():
        """local function"""
        a = "hello"
        b = "world"
        return a+b
    x = 1
    y = 2
    return x+y


store = []


def sort_by_last_letter(string):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(string, key=last_letter)


# Local, Global, Enclosing, Built-in, (LEGB) rule
g = 'global'

def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(func1())
    # print(func2())
    s = ['hello', 'how', 'are', 'you']
    # print(sort_by_last_letter(s))
    # print(sort_by_last_letter(s))
    # print(sort_by_last_letter(s))
    # print(store)    # prints the list of addresses for this function
    # printed multiple times to indicate different addresses, every
    # single time

    outer()




# --------------------------------------------------
if __name__ == '__main__':
    main()
