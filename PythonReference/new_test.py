import unittest
from main import mergesort

class TestFunctions(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(mergesort([5,4,3,2,1]), [1, 2, 3, 4, 5])
        self.assertEqual(mergesort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mergesort([34, 21, 23, 34, 86, 34]), [21, 23, 34, 34, 34, 86])
        self.assertEqual(mergesort([2, 2, 2, 2, 2, 1]), [1, 2, 2, 2, 2, 2])
    
unittest.main()