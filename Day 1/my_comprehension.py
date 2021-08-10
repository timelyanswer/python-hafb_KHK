#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

def is_prime(x):
    """

    Returns true or false in inputs is a prime number
    :param x: integer
    :return: True or False
    """
from math import sqrt
from pprint import pprint as pp


if x < 2:
        return False
    for i in range (2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
        return True



# --------------------------------------------------
def main():
    """iterables and comprehensions"""

    words = "today i am very happy because barcelona does not have Messi with them any more".split()
    #print(words)
    lwords = []
     print(words)
    for word in words:
        lwords.append(len(word))
        print(lwords)
       list Comprehension
       totals = [len(word) for word in words]
       print(totals)

        prime_nums = [x for x in range(1001) if is_prime(x)]
        print(prime_nums)
    print(sum(prime_nums))






# --------------------------------------------------
if __name__ == '__main__':
    main()
