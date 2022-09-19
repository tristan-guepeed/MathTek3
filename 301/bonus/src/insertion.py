#!/usr/bin/env python3

import time

def insertion(numbers, tps):
    insertionsort = 0
    retenu = 0
    select = numbers
    i, j, a = 0, 1, 0
    select = []
    while (a != len(numbers)):
        select.append(numbers[a])
        a+=1
    #print(select)
    tps1 = time.time()
    while (j != len(select)):
        i = 0
        retenu = select[j]
        while (i < j):
            insertionsort += 1
            if (retenu < select[i]):
                break
            i += 1
        select.insert(i, retenu)
        del select[j + 1]
        j+=1
    tps2 = time.time()
    tps.append(tps2 - tps1)
    #print(select)
    print("Insertion sort: ", end="")
    print(insertionsort, end="")
    print(" comparisons")

    return insertionsort