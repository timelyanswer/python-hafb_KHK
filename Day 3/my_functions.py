#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose: discuss callable objects, callable instances and lambdas
"""
import socket


def resolve(host):
    return socket.gethostname(host)



class Resolver:
    def __init__(self):
        self._cache = {}


    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

def sequence_class(immutable):
    # if immutable:
    #    cls = tuple
    #else:
    #    cls = list
    # return cls

    # the below code is the same as the one above
    return tuple if immutable else list

def test_lambda():
    scientist = ['Marie Curie',
                 'Albert Einstein',
                 'Niel Bohr',
                 'Dimitri Mendeleev',
                 'Charles Darwin',
                 'Isaac Newton']

    # print sorting by last name
    pp(sorted(scientist, key=lambda name: name.split()[-1]))

    # print sorting by first name
    pp(sorted(scientist))







# --------------------------------------------------
def main():
    """Make your noise here"""
    resolve = Resolver()
    # print(resolve)
    print(resolve('weber.edu'))
    print(resolve('google.com'))

    resolve.clear()

    resolve = Resolver()
    print(resolve('google.com'))
    print(resolve.__call__('yahoo.com'))



# --------------------------------------------------
if __name__ == '__main__':
    main()
