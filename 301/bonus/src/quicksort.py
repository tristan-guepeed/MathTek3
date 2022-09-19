#!/usr/bin/env python3

import time

def quickSort(numbers):
    quick, check = 0, numbers
    if len(check) <= 1:
        return check, quick
    pivot = check[0]
    left, right= [], []
    i = 1
    while (i < len(check)):
        quick+=1
        if check[i] >= pivot:
            left.append(check[i])
        else:
            right.append(check[i])
        i+=1
    left = quickSort(left)
    right = quickSort(right)
    quick += left[1] + right[1]
    return check, quick

def quicksort(numbers, tps):
    tps1 = time.time()
    quick = quickSort(numbers)[1]
    tps2 = time.time()
    tps.append(tps2 - tps1)
    print("Quicksort: ", end="")
    print(quick, end="")
    print(" comparisons")

    return quick