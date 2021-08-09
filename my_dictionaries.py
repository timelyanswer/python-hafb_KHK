#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from pprint import pprint as pp

import argparse


# --------------------------------------------------

def main():
    """Review Dictionaries"""

    urls = {'Google':"http://google.com",
            'Twitter': 'http://twitter.com',
            'WSU': 'http://weber.edu'}

    print(type(urls))
    print(urls)
    # curls = urls.copy()
    urls['WSU']= 'http://weber.edu.tmp'
    print(urls)
    urls['yahoo'] = 'http://yahoo.com'
    print(urls)
    # to iterate

    # for key in urls:
    # iterate over values which is shown

       for key, value in urls.items():
        print(f'values => {value}')
        # print(f'{key}=>{urls[key]}')

        for key, value in urls.items():
            print(f'{key} =>{value}')

            pp(urls)





# --------------------------------------------------
if __name__ == '__main__':
    main()
