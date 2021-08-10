#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

class SortedSet:
    def __init__(self, items = None):
        """
        create a sorted list, regardless of which
        iterable object you passed
        :param items: list of items
        """

        self.items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """ Container Protocol"""
        return item in self._items

    def __len__(self):
        """ length protocol """
        return len(self._items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self._items[index]

    # slicing
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], Sorted([1, 4, 9]))









# --------------------------------------------------
def main():
    """Make your noise here"""

    pass



# --------------------------------------------------
if __name__ == '__main__':
    main()
