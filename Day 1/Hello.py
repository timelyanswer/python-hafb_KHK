# python-hafb_KHK

## Instructor project
http://github.com/jik-wsu/python-hafb_KHK

## Local installations

Login to system using:
- Username: **txx** (xx is terminal number)
- Password: **Hello123**

Need to open git bash and run the following comma
```bash
pip install pytest
```
Reload 'Pycharm'

## Setup pytest to run in `Powershell`
"""
Author: Jeong Kim
Purpose: Say Hello to Waldo
"""

import argparse

def get_args():
    """

    Get the command-line arguments
    :return: list of parsed arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()

# add pass for an extra line python expects 2 lines of code in

def main ():
    """
    This is where the actions is, python expects 2 lines of code
    at all times, use 'pass'
    :return: None
    """
    args = get_args()
    print('Hello,  ' + args.name + '!')


if __name__== '__main__':
    main()

