#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs= '+'      #one or more arguments
                        help='A positional argument')

    parser.add_argument('-a',
                        '--sorted',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action= 'store_true',
                        help='Sort the items')

    return parser.parse_args()



# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    print(args.item)
    # TODO:  check if the list needs to be sorted

    #  TODO: prepare list ot print
    #   1 Item, just pringt item
    #   2 Items: item1 and item2
    #   3 or more Items: item1, item2, itemX, and itemLast

    bringing = ' '

    #   Print info

    print(f'You are brining {bringing}')

    arg = '" "'
    out = getoutput(f'{prg} {arg}')

    def test_usage():
        """usage"""

        for flag in ['', '-h', '--help']:
            out = getoutput(f'{prg} {flag}')
            assert out.lower().startswith('usage')


    def test_two():
        """two items"""

        out = getoutput(f'{prg} soda "french fries"')
        assert out.strip() == 'You are bringing soda and french fries.'



# --------------------------------------------------
if __name__ == '__main__':
    main()
