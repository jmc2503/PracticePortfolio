import unittest
from main import add, divide

class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, -3), -4)
        self.assertIsInstance(add(1,4), int)
    
    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
        



if __name__=="__main__":
    unittest.main()