#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


parser.add_argument('fname',
                    metavar='str',
                    help='a file to read')

return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    str_arg = args.fname
    print(f'str_arg = {str_arg}"')








# --------------------------------------------------
if __name__ == '__main__':
    main()
