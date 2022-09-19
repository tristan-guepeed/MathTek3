#!/usr/bin/env python3

from math import *

def draw_all(allVectors, allAbscissas, allRadius):
    print("vector result: [", end='')
    i = 0
    while (i < len(allVectors)):
        if (allVectors[i] > -0.1 and allVectors[i] < 0.1):
            print("0.0", end='')
        else:
            print("%.1f" % allVectors[i], end='')
        if (i + 1 < len(allVectors)):
            print(", ", end='')
        i = i + 1
    print("]")
    i = 0
    while (i < len(allAbscissas)):
        print("abscissa: %.1f cm\tradius: %.1f cm" % (allAbscissas[i], allRadius[i]))
        i = i + 1
    return (0)

def get_vectors(argv):
    allVectors = [0, 0, 0, 0, 0]

    A = 6 * (float(argv[3]) - 2 * float(argv[2]) + float(argv[1])) / 50;
    B = 6 * (float(argv[4]) - 2 * float(argv[3]) + float(argv[2])) / 50;
    C = 6 * (float(argv[5]) - 2 * float(argv[4]) + float(argv[3])) / 50;
    allVectors[2] = (B - (A + C) / 4) * 4 / 7;
    allVectors[1] = A / 2 - 0.25 * allVectors[2];
    allVectors[3] = C / 2 - 0.25 * allVectors[2];
    
    return (allVectors)

def get_abscissas(n):
    allAbscissas = []
    step = float(20 / (n - 1))

    allAbscissas.append(0)
    i = 1
    while (len(allAbscissas) < n):
        allAbscissas.append(step * i)
        i = i + 1
    return (allAbscissas)

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
    
def pipes(argv):
    allVectors = get_vectors(argv)
    allAbscissas = get_abscissas(int(argv[6]))
    allRadius = get_radius(allVectors, int(argv[6]), argv)

    draw_all(allVectors, allAbscissas, allRadius)
    return (0)
