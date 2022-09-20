#!/usr/bin/env python3

def get_radius(allVectors, n, argv):
    allRadius = []
    allArg = [float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5])]
    allBaseValue = [0, 5, 10, 15, 20]
    i = 1

    allRadius.append(float(argv[1]))
    while (i < n):
        x = 20 / (n - 1) * i
        a = int(((x - 0.01) / 5)) + 1
        tmp = (-allVectors[a - 1] / 30 * pow(x - allBaseValue[a], 3)
               + allVectors[a] / 30 * pow(x - allBaseValue[a - 1], 3)
               - (allArg[a - 1] / 5 - 5 / 6 * allVectors[a - 1])
               * (x - allBaseValue[a])
               + (allArg[a] / 5 - 5 / 6 * allVectors[a])
               * (x - allBaseValue[a - 1]))
        allRadius.append(tmp)
        i = i + 1

    return (allRadius)
