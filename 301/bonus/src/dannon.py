#!/usr/bin/env python3

from src.selection import selection
from src.insertion import insertion
from src.bubble import bubble
from src.quicksort import quicksort
from src.merge import mergesort
import matplotlib.pyplot as plt

def dannon(numbers):
    tps = []
    print(len(numbers), end="")
    print(" elements")
    selectionsort = selection(numbers, tps)
    insertionsort = insertion(numbers, tps)
    bubblesort = bubble(numbers, tps)
    quick = quicksort(numbers, tps)
    merge = mergesort(numbers, tps)

    names = ['Selection', 'Insertion', 'Bubble', 'Quick', 'Merge']
    values = [selectionsort, insertionsort, bubblesort, quick, merge]
    plt.subplot(131)
    plt.bar(names, values)
    plt.suptitle('Number of elementary operations performed by five differents algorithms (left) and time to execute those algorithms')
    plt.subplot(133)
    plt.bar(names, tps)
    plt.show()
    return 0