#!/usr/bin/env python3

merge = 0

def mergeSort(numbers):
    global merge

    if (len(numbers) > 1):
        leftside = len(numbers) // 2
        rightside = len(numbers) // 2
        semileft = numbers[leftside:]
        semiright = numbers[:rightside]
        semileft = mergeSort(semileft)
        semiright = mergeSort(semiright)
        numbers = []

        while (len(semileft) > 0 and len(semiright) > 0):
            if (semileft[0] < semiright[0]):
                numbers.append(semileft[0])
                semileft.pop(0)
            else:
                numbers.append(semiright[0])
                semiright.pop(0)
            merge+=1
        i = 0
        while (i < len(semileft)):
            numbers.append(semileft[i])
            i+=1
        i = 0
        while (i < len(semiright)):
            numbers.append(semiright[i])
            i+=1
    return numbers

def mergesort(numbers):
    global merge

    mergeSort(numbers)
    print("Mergesort: ", end="")
    print(merge, end="")
    print(" comparisons")

    return merge