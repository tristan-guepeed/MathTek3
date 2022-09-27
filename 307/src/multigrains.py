#!/usr/bin/env python3

from src.calc import calc

def matrix_zob(number_list, price_list):
    grains = [[1, 1, 2, 0], [0, 2, 1, 0], [1, 0, 0, 3], [0, 1, 1, 1], [2, 0, 0, 2]]
    matrix = []

    matrix.append([grains[0][0], grains[1][0], grains[2][0], grains[3][0], grains[4][0], 1, 0, 0, 0, number_list[0]])
    matrix.append([grains[0][1], grains[1][1], grains[2][1], grains[3][1], grains[4][1], 0, 1, 0, 0, number_list[1]])
    matrix.append([grains[0][2], grains[1][2], grains[2][2], grains[3][2], grains[4][2], 0, 0, 1, 0, number_list[2]])
    matrix.append([grains[0][3], grains[1][3], grains[2][3], grains[3][3], grains[4][3], 0, 0, 0, 1, number_list[3]])
    matrix.append([-price_list[0], -price_list[1], -price_list[2], -price_list[3], -price_list[4], 0, 0, 0, 0, 0])
    return matrix

def finalPrint(number_list, price_list, result, total):
    print("Resources: %d F1, %d F2, %d F3, %d F4\n" %(number_list[0], number_list[1], number_list[2], number_list[3]))
    print("Oat: %d units at $%d/unit" % (result[0], price_list[0]) if result[0] == 0 else "Oat: %.2f units at $%d/unit" % (result[0], price_list[0]))
    print("Wheat: %d units at $%d/unit" % (result[1], price_list[1])  if result[1] == 0 else "Wheat: %.2f units at $%d/unit" % (result[1], price_list[1]))
    print("Corn: %d units at $%d/unit" % (result[2], price_list[2])  if result[2] == 0 else "Corn: %.2f units at $%d/unit" % (result[2], price_list[2]))
    print("Barley: %d units at $%d/unit" % (result[3], price_list[3])  if result[3] == 0 else "Barley: %.2f units at $%d/unit" % (result[3], price_list[3]))
    print("Soy: %d units at $%d/unit" % (result[4], price_list[4])  if result[4] == 0 else "Soy: %.2f units at $%d/unit\n" % (result[4], price_list[4]))
    print("Total production value: $%.2f" % total)

def multigrains(argv):
    n1 = int(argv[1])
    n2 = int(argv[2])
    n3 = int(argv[3])
    n4 = int(argv[4])
    poat = int(argv[5])
    pwheat = int(argv[6])
    pcorn = int(argv[7])
    pbarley = int(argv[8])
    psoy = int(argv[9])
    number_list = [n1, n2, n3, n4]
    price_list = [poat, pwheat, pcorn, pbarley, psoy]
    matrix = matrix_zob(number_list, price_list)
    order = calc(matrix)
    resultOrder = [0] * 5
    for i in [0, 1, 2, 3]:
        if order[i] != -1:
            resultOrder[order[i]] = matrix[i][len(matrix[i]) - 1]
    finalPrint(number_list, price_list, resultOrder, matrix[-1][-1])
    return 0