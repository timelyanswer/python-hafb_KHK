#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
import sys




# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())
    # writing to file, wt stands for writing text
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.write('this is the first line of text i have here.\n')
    f.write('here is the second line of text i have.\n')
    f.close()

    #reading files below
    g = open('wasteland.txt', mode='wt', encoding='utf-8')
    info = g.read(27)
    print(info)
    info = g.read()     # reads the rest
    print(info)
    g.close()


    #read all lines
    g = open('wasteland.txt', mode='wt', encoding='utf-8')
    info = g.readlines()  # reads 27 bites
    print(f'[{info}]')
    g.close()

    # appending text to files
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.writelines(['son of man\n,'
                  'there is another one,',
                  'here it is again,'])
    f.close()



    # anytime using the open code, make sure you close it

    # print(type(f))

    # here is the close function
    # f.close()










# --------------------------------------------------
if __name__ == '__main__':
    main()
