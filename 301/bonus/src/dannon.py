#!/usr/bin/env python3

from src.selection import selection
from src.insertion import insertion
from src.bubble import bubble
from src.quicksort import quicksort
from src.merge import mergesort
import matplotlib.pyplot as plt

def dannon(numbers):
    print(len(numbers), end="")
    print(" elements")
    selectionsort = selection(numbers)
    insertionsort = insertion(numbers)
    bubblesort = bubble(numbers)
    quick = quicksort(numbers)
    merge = mergesort(numbers)

    names = ['Selection', 'Insertion', 'Bubble', 'Quick', 'Merge']
    values = [selectionsort, insertionsort, bubblesort, quick, merge]
    plt.subplot(132)
    plt.bar(names, values)
    plt.suptitle('Number of elementary operations performed by five differents algorithms')
    plt.show()
    return 0