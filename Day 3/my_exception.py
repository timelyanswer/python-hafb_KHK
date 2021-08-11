#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
import encodings.cp437
from random import randrange

def more_info():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print(f'encoding: {e.encoding}')
        print(f'reason: {e.reason}')
        print(f'object: {e.object}')
        print(f'start: {e.start}')
        print(f'end: {e.end}')

def median(iterable)
    """obtain the central value of a series
    sort the iterable and return the middle value if
    there is an odd number of elements, or the arithmetic 
    mean of the middle two elements if there is an
    even number of elements
    """

    items = sorted(iterable)
    median_index = len(items) - 1) // 2.0
    if len(items) % 2 != 0:
        return items[median_index]
    else:
        return (items[median_index] + items[median_index+1])/2.0

def test_median():
    # print(f'Median odd= {median([5, 2, 1, 4, 3])}')
    # print(f'Median even= {median([5, 2, 1, 4, 3, 6])}')
    # print(f'Median empty= {median([])}')

    try:
        median([])
    except ValueError as e:
        print(f'Payload: {e.args}')
        print(f'{str(e)}')





def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print('Handled IndexError')

    d = dict(a=65, b=33)
    try:
        value = d['x']
    except LookupError:
        print('Handled KeyError')




# --------------------------------------------------


# --------------------------------------------------
def main():
    """Make your noise here"""
    # random number from 0 to 10
   # number = randrange(10)

    #while True:
     #   try:
      #      guess = int(input('number?'))
       # except ValueError:
        #    continue
         #   if guess == number:
          #      print('you got it')
           # break









# --------------------------------------------------
if __name__ == '__main__':
    main()
    lookups()

