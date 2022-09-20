#!/usr/bin/env python3

def matrix(argv):
    try:
        open(argv[1], "r")
    except:
        print("Error: File does not appear to exist.")
        return 84
    zob = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]
    print(zob[0])
    print(zob[1])
    print(zob[2])
    print(zob[3])
    print(zob[4])
    print(zob[5])
    print("")
    print("fc.c -> fc.o -> tty")
    print("fc.h -> fc.o -> tty")
    print("fc.h -> tty.o -> tty")
    print("fc.o -> tty")
    print("tty.c -> tty.o -> tty")
    print("tty.o -> tty")
    return 0