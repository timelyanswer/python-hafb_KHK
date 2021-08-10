import unittest
from sorted_set import SortedSet



class TestConstructor(unittest.TestCase):

class TestContainerProtocol(unittest.TestCase):


class TestSizeProtocol(unittest.TestCase):


class TestIterableProtocol(unittest.TestCase):


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
        self.s[5]



    def setUp(self):
        self.s = SortedSet([7, 2, 1, 1, 9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for loop(self):
    index = 0
    expected = [1, 2, 7, 9]
    for item in self.s:
        self.assertEqual(item, expected[index])
        index += 1




if __name__ == '__main__':
    main()
