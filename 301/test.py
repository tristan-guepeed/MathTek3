#!/usr/bin/env python3

import unittest

from src.dannon import dannon


class TestDannon(unittest.TestCase):
    def test_list_int(self):
        data = [3.3, 5, 9.89, -6]
        result = dannon(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
