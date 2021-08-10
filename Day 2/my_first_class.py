#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose: review basics of classes
"""

class Point:
    """ represents a point in a 2-d geometric coordinates"""
    def __init__(self, x=0, y=0):

        pass

    def reset(self):
        """ resets the point to the new location in 2d space"""
        #self._x = 0 # for "private" use _
        #self._y = 0
        self.move(0, 0)

    def move (self, x, y):
        """ move point to a new location in 2d space
            :param x: x-coordinate
            :param x: y-coordinate
            :return: nothing
        """
        self._x = x
        self._y = y

    def calculate_distance(self, other_point):

        # self._x = () **2
        # self._y = () **2
        # calculate_distance = sqrt(self._x + self_y)
        return sqrt((self._x - other_point._x)**2 + (self._y - other_point._y)**2)










# --------------------------------------------------
def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point()
    # <object,>.<attribute> = <value>
    #p1._x = 5
    #p1._y = 4
    #p2._x = 3
    #p2._y = 9
    print(p1._x, p1._y)
    print(p2._x, p2._y)
    p2.reset()          # reset values
    print(p2._x, p2._y)
    p2.move(3,3)
    # print(p2.move(self, p1._x, p1._y))
    assert(p2.calculate_distance(p1) == p1.calculate_distance(p2))
    p1.move(2, -4)
    print(p1.calculate_distance(p2))
    print(p1.calculate_distance(p1))








# --------------------------------------------------
if __name__ == '__main__':
    main()
