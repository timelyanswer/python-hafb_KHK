#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review itertools package
"""
from itertools import islice, count
from math import sqrt

def is_prime(x):

    if x < 2:
        return False
        for i in range(2, int(sqrt(x)) +1):
            if x % i == 0:
                return False
            return True




# --------------------------------------------------
def main():
    """Make your noise here"""
    # Task: Create a list of the first 1000 prime numbers

    # thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    # print(thousand_primes)


    #Use the built-ins any, all
    print(any([False, False, True]))
    print(all([False, False, True]))
    cities = ['London', 'Madrid', 'New York', 'Ogden']
    print(f'the cities list is{all(city ==city.title() for city in cities)} to go')

    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 22, 24, 28, 22, 20, 18, 22]

    # for item in zip(sunday, monday):
    for sun, mon in zip(sunday, monday):
        print(f'the average for sunday and monday ={(sun+mon)/2.0}')


    for temp in zip(sunday, monday, tuesday):
        print(f'minimum ={min(temp)}, maximum ={max(temp)} and avg = {sum(temp)/len(temp)}')
        print(f'minimum ={min(temp):4.1f}, maximum ={max(temp):4.1f} and avg = {sum(temp)/len(temp):4.1f}')

        #print(f'minimum ={:4.1f}, maximum ={:4.1f} and avg = {:4.1f}'.format(min(temp), max(temp), sum))














# --------------------------------------------------
if __name__ == '__main__':
    main()
