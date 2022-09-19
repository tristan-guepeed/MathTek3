#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from src.dannon import dannon
from src.selection import selection
from src.insertion import insertion
from src.bubble import bubble
from src.quicksort import quicksort
from src.merge import mergesort
from src.parsing import check_error


class TestDannon(unittest.TestCase):
    def test_principal_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = dannon(data)
        self.assertEqual(result, 0)

    def test_selection_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = selection(data)
        self.assertEqual(result, 0)

    def test_selection_func_return2(self):
        data = [-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]
        result = selection(data)
        self.assertEqual(result, 0)

    def test_insertion_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = insertion(data)
        self.assertEqual(result, 0)

    def test_insertion_func_return2(self):
        data = [-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]
        result = insertion(data)
        self.assertEqual(result, 0)

    def test_bubble_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = bubble(data)
        self.assertEqual(result, 0)

    def test_bubble_func_return2(self):
        data = [-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]
        result = bubble(data)
        self.assertEqual(result, 0)

    def test_quick_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = quicksort(data)
        self.assertEqual(result, 0)

    def test_quick_func_return2(self):
        data = [-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]
        result = quicksort(data)
        self.assertEqual(result, 0)

    def test_merge_func_return(self):
        data = [3.3, 5, 9.89, -6]
        result = mergesort(data)
        self.assertEqual(result, 0)

    def test_merge_func_return2(self):
        data = [-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]
        result = mergesort(data)
        self.assertEqual(result, 0)

    def test_parsing_func_return(self):
        data = ["./301dannon","../test3"]
        result = check_error(data)
        self.assertEqual(result, [3.3, 5, 9.86, -6])

    def test_parsing_func_return_no_existing_file(self):
        data = ["./301dannon","random"]
        result = check_error(data)
        self.assertEqual(result, 84)

    def test_parsing_func_return_need_two_args(self):
        data = ["./301dannon"]
        result = check_error(data)
        self.assertEqual(result, 84)

    def test_parsing_func_return_help(self):
        data = ["./301dannon","-h"]
        result = check_error(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
