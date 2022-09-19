#!/usr/bin/env python3

def insertion(numbers):
    insertionsort = 0
    passe = 0
    retenu = 0
    select = numbers
    i, j, a = 0, 1, 0
    select = []

    while (a != len(numbers)):
        select.append(numbers[a])
        a+=1
    #print(select)
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
    #print(select)
    print("Insertion sort: ", end="")
    print(insertionsort, end="")
    print(" comparisons")

    return insertionsort