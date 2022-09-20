#!/usr/bin/env python3

def get_abscissas(n):
    allAbscissas = []
    step = float(20 / (n - 1))

    allAbscissas.append(0)
    i = 1
    while (len(allAbscissas) < n):
        allAbscissas.append(step * i)
        i = i + 1
    return (allAbscissas)
