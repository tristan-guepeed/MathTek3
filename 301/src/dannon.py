#!/usr/bin/env python3

from src.selection import selection
from src.insertion import insertion
from src.bubble import bubble
from src.quicksort import quicksort
from src.merge import mergesort

def dannon(numbers):
    print(len(numbers), end="")
    print(" elements")
    selection(numbers)
    insertion(numbers)
    bubble(numbers)
    quicksort(numbers)
    mergesort(numbers)
    return 0