import unittest

import functions.functions as functions


class FunctionsTests(unittest.TestCase):
    def test_print_hi(self):
        self.assertEqual('Hi, PyCharm', functions.print_hey('PyCharm'))  # add assertion here

    def test_addition(self):
        self.assertEqual(4, functions.addition(2, 2))

    def test_subtraction(self):
        self.assertEqual(0, functions.sub(2, 2))


if __name__ == '__main__':
    unittest.main()
