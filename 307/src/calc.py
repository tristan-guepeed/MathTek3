#!/usr/bin/env python3

def find(matrix):
    if (len(matrix) <= 0 or len(matrix[0]) <= 5):
        return (-1, -1)
    vY, vX = len(matrix), len(matrix[0])
    line = matrix[vY - 1]
    copy = line[0:5]
    Min = min(copy)
    if Min >= 0:
        return (-1, -1)
    zob2 , zob = copy.index(Min), -1
    Min = 9999999999
    for i in range(0, vY - 1):
        if (matrix[i][vX - 1]):
            if (matrix[i][zob2] > 0 and (Min > matrix[i][vX - 1] / matrix[i][zob2] and matrix[i][vX - 1] / matrix[i][zob2] > 0)):
                zob = i
                Min = matrix[i][vX - 1] / matrix[i][zob2]
        elif Min > matrix[i][zob2] and matrix[i][zob2] > 0:
            zob = i
            Min = matrix[i][vX - 1] / matrix[i][zob2]
    return (zob, zob2)

def use(matrix, zob, zob2):
    point = matrix[zob][zob2]
    for a in range(len(matrix[zob])):
        matrix[zob][a] = matrix[zob][a] / point
    maxY, maxX = len(matrix), len(matrix[0])
    for i in range(maxY):
        if i == zob:
            continue
        v = matrix[i][zob2]
        for j in range(maxX):
            matrix[i][j] -= v * matrix[zob][j]

def calc(matrix):
    order = [-1, -1, -1, -1]
    i = 0

    while (1 != 0):
        i += 1
        if i == 6:
            break
        zob, zob2 = find(matrix)
        if (zob2 < 0 or zob < 0):
            break
        use(matrix, zob, zob2)
        order[zob] = zob2
    return order