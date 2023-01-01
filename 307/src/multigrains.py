#!/usr/bin/env python3


def matrix_zob(number_list):
    grains = [[1, 1, 2, 0], [0, 2, 1, 0], [1, 0, 0, 3], [0, 1, 1, 1], [2, 0, 0, 2]]
    matrix = []

    matrix.append([grains[0][0], grains[1][0], grains[2][0], grains[3][0], grains[4][0], 1, number_list[0]])
    matrix.append([grains[0][1], grains[1][1], grains[2][1], grains[3][1], grains[4][1], 2, number_list[1]])
    matrix.append([grains[0][2], grains[1][2], grains[2][2], grains[3][2], grains[4][2], 3, number_list[2]])
    matrix.append([grains[0][3], grains[1][3], grains[2][3], grains[3][3], grains[4][3], 4, number_list[3]])
    return matrix

def finalPrint(number_list, price_list):
    print ("resources:  %d F1, %d F2, %d F3, %d F4" % (number_list[0], number_list[1], number_list[2], number_list[3]))
    print ("\noatmeal:  X units at € %d /unit" % (price_list[0]))
    print ("wheat:  X units at € %d /unit" % (price_list[1]))
    print ("corn:  X units at € %d /unit" % (price_list[2]))
    print ("barley:  X units at € %d /unit" % (price_list[3]))
    print ("soy:  X units at € %d /unit" % (price_list[4]))
    print ("total production value: € X")

def multigrains(argv):
    f1 = int(argv[1])
    f2 = int(argv[2])
    f3 = int(argv[3])
    f4 = int(argv[4])
    poat = int(argv[5])
    pwheat = int(argv[6])
    pcorn = int(argv[7])
    pbarley = int(argv[8])
    psoy = int(argv[9])
    number_list = [f1, f2, f3, f4]
    price_list = [poat, pwheat, pcorn, pbarley, psoy]
    matrix = matrix_zob(number_list)
    finalPrint(number_list, price_list)
    return 0