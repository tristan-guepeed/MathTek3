#!/usr/bin/env python3

import time

def bubble(numbers, tps):
    a, i, j, retenu, k, bubblesort = 0, 0, 1, 0, 0, 0
    select = []
    while (a != len(numbers)):
        select.append(numbers[a])
        a+=1
    #print(select)
    tps1 = time.time()
    while (k != len(select)):
        while (j < (len(select) - k)):
            bubblesort+=1
            if (select[i] > select[j]):
                retenu = select[j]
                select[j] = select[i]
                select[i] = retenu
            i+=1
            j+=1
        k+=1
        j = 1
        i = 0
    tps2 = time.time()
    tps.append(tps2 - tps1)
    #print(select)
    print("Bubble sort: ", end="")
    print(bubblesort, end="")
    print(" comparisons")

    return bubblesort