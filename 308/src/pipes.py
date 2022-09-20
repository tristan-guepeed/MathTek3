#!/usr/bin/env python3

from math import *
from src.vectors import get_vectors
from src.abscissas import get_abscissas
from src.radius import get_radius

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

def pipes(argv):
    allVectors = get_vectors(argv)
    allAbscissas = get_abscissas(int(argv[6]))
    allRadius = get_radius(allVectors, int(argv[6]), argv)

    draw_all(allVectors, allAbscissas, allRadius)
    return (0)
