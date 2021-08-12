#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: practice basics of numpy
"""

import numpy as np

def np_arrays():
    array_one = np.array([1, 2, 3, 4])
    print(array_one, type(array_one))
    numbers = [9, 7, 10, 12]
    print(numbers, type(numbers))
    array_two = np.array(numbers)
    print(array_two, type(array_two))
    # create arrays with initial placeholders
    array_of_zeros = np.zeros((3, 4))
    print(array_of_zeros)
    array_of_ones = np.ones((3, 4))
    print(array_of_ones)
    array_of_empty = np.empty((3, 4))
    print(array_of_empty)
    array_of_ones = np.ones((3, 4))
    print(array_of_ones)
    array_eye = np.eye(3)
    print(array_eye)
    array_of_events = np.arange(0, 2, 0.3)
    print(array_of_events)
    array_of_events = np.arange(0, 2, 0.3)
    print(array_of_events)
    array_nd = np.arange(6).reshape(2, 3)
    print(array_nd)






# --------------------------------------------------
def main():
    """Make your noise here"""
    np_arrays()



# --------------------------------------------------
if __name__ == '__main__':
    main()
