#!/usr/bin/env python3

def get_vectors(argv):
    allVectors = [0, 0, 0, 0, 0]

    tmp1 = 6 * (float(argv[3]) - 2 * float(argv[2]) + float(argv[1])) / 50;
    tmp2 = 6 * (float(argv[4]) - 2 * float(argv[3]) + float(argv[2])) / 50;
    tmp3 = 6 * (float(argv[5]) - 2 * float(argv[4]) + float(argv[3])) / 50;
    allVectors[2] = (tmp2 - (tmp1 + tmp3) / 4) * 4 / 7;
    allVectors[1] = tmp1 / 2 - 0.25 * allVectors[2];
    allVectors[3] = tmp3 / 2 - 0.25 * allVectors[2];

    return (allVectors)
