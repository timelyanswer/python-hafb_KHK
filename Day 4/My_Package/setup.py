#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""
from distutils.core import setup

setup(
    name='class_decorator',
    version='0.1',
    py_modules=['my_class_decorator'],      # need my_xxx so it does not confuse with the other
    #Metadata
    author='Waldo Weber',
    author_email='waldo@weber.edu',
    description='A module that shows how to use Class Decorators',
    license='Public domain',
    keywords='decorators',
)




# --------------------------------------------------
def main():
    """Make your noise here"""



# --------------------------------------------------
if __name__ == '__main__':
    main()
