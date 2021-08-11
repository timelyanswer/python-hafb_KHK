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

        self._items = sorted(set(items)) if items is not None else []

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

    def __getitem__(self, index):
        print(index)
        print(type(index))
        return self._items[index]

    def __repr__(self):
        return 'SortedSet({})'.format(
            repr(self._items) if self._items else '')

    # slicing
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], Sorted([1, 4, 9]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], Sorted([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], Sorted())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], Sorted([9, 13]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)


# --------------------------------------------------
def main():
    """Make your noise here"""

    pass



# --------------------------------------------------
if __name__ == '__main__':
    main()
