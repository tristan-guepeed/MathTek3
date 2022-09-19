#!/usr/bin/env python3

def selection(numbers):
    selectionsort = 0
    retenu = -1
    retenu2 = 0.0
    i, j, k, a = 0, 1, 1, 0
    select = []
    while (a != len(numbers)):
        select.append(numbers[a])
        a+=1
    #print(select)
    while (i != len(select) - 1):
        while (j < len(select)):
            if (select[i] > select[j]):
                if (retenu != -1):
                    if (select[retenu] > select[j]):
                        retenu = j
                else:
                    retenu = j
            j+=1
            selectionsort+=1
        if (retenu == -1):
            i+=1
            j = k + 1
            k+=1
        else:
            j = k + 1
            k+=1
            retenu2 = select[retenu]
            select[retenu] = select[i]
            select[i] = retenu2
            i+=1
        retenu = -1
    #print(select)
    print("Selection sort: ", end="")
    print(selectionsort, end="")
    print(" comparisons")
    return 0