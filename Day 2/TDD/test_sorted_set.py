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


class TestReprProtocol(unittest.TestCase):
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), 'SortedSet()')

    def test_repr_some(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), 'SortedSet([19, 40, 42])')

class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([1, 2, 3]) == SortedSet ([1, 2, 3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([1, 2, 3]) == SortedSet([4, 5, 6]))

   def test_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [4, 5, 6])

   def test_identical(self):
       s = SortedSet([1, 2, 3])
       self.assertTrue(s == s)

  def test_mismatch_unequal(self):
       s = SortedSet([1, 2, 3])
       self.assertTrue(SortedSet([1, 2, 3] != SortedSet ([4, 7, 10])))




def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet)
            return NotImplemented
        return self.items == rhs._items









if __name__ == '__main__':
    main()
