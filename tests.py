import unittest

from main import print_hey, addition, sub


class MyTestCase(unittest.TestCase):
    def test_print_hi(self):
        self.assertEqual('Hi, PyCharm', print_hey('PyCharm'))  # add assertion here

    def test_addition(self):
        self.assertEqual(4, addition(2, 2))

    def test_subtraction(self):
        self.assertEqual(0, sub(2, 2))


if __name__ == '__main__':
    unittest.main()
