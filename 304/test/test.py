#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from src.parsing import check_error
from src.pathfinding import pathfinding

class TestPacman(unittest.TestCase):
    def test_parsing1(self):
        result = check_error(["./304pacman", "map1"])
        self.assertEqual(result, 84)
    def test_parsing2(self):
        result = check_error(["./304pacman", "../map1", "e", "e"])
        self.assertEqual(result, 84)
    def test_parsing3(self):
        result = check_error(["./304pacman", "../map1", "o", " "])
        self.assertEqual(result, 0)
    def test_parsing4(self):
        result = check_error(["./304pacman", "../map1", "ee", "rr"])
        self.assertEqual(result, 84)
    def test_parsing5(self):
        result = check_error(["./304pacman", "-h"])
        self.assertEqual(result, 1)
    def test_parsing6(self):
        result = check_error(["./304pacman", "NO", "ee", "rr"])
        self.assertEqual(result, 84)
    def test_basic_test(self):
        result = pathfinding(["./304pacman", "../map1", "o", " "])
        self.assertEqual(result, 0)
    def test_basic_test(self):
        result = pathfinding(["./304pacman", "../map2", "o", " "])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
