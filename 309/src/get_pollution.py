#!/usr/bin/env python3

from math import *
from src.get_file import get_file

def get_file_value(filename):
    fileContent = get_file(filename)
    i = 0
    values = []

    while (i < len(fileContent)):
        tmpValues = []
        tmp = ""
        ii = 0
        while (fileContent[i][ii] != ';'):
            tmp = tmp + fileContent[i][ii]
            ii = ii + 1
        tmpValues.append(int(tmp))
        tmp = ""
        ii = ii + 1
        while (fileContent[i][ii] != ';'):
            tmp = tmp + fileContent[i][ii]
            ii = ii + 1
        tmpValues.append(int(tmp))
        tmp = ""
        ii = ii	+ 1
        while (ii < len(fileContent[i])):
            tmp = tmp + fileContent[i][ii]
            ii = ii + 1
        tmpValues.append(int(tmp))
        values.append(tmpValues)
        i = i + 1
    return (values)

def get_grid(filename, n):
    values = get_file_value(filename)
    grid = []
    i = 0
    while (i < n):
        grid.append([0] * n)
        i = i + 1
    i = 0
    while (i < len(values)):
        grid[values[i][1]][values[i][0]] = values[i][2]
        i = i + 1
    return (grid)

def formule(n, idx, pos):
    a = int(factorial(n) / (factorial(idx) * factorial(n - idx)))
    b = 0
    if (idx != 0):
        b = pow(pos, idx)
    else:
        b = 1
    if ((n - idx) != 0):
        c = pow((1 - pos), (n - idx))
    else:
        c = 1
    return (a * b * c)

def bezier_surfaces(x, y, grid, n):
    total_pollution = 0
    i = 0
    while (i < (n + 1)):
        ii = 0
        while (ii < (n + 1)):
            current_pollution = grid[i][ii] * formule(n, i, y) * formule(n, ii, x)
            total_pollution = total_pollution + current_pollution
            ii = ii + 1
        i = i + 1
    return (total_pollution)

def get_pollution(argv):
    n = int(argv[1])
    x = float(argv[3]) / (n - 1)
    y = float(argv[4]) / (n - 1)
    grid = get_grid(argv[2], n)
    print("%.2f" % bezier_surfaces(x, y, grid, n - 1))
    return (0)
