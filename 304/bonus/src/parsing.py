#!/usr/bin/env python3

from src.get_file import get_file

def print_help():
    print("USAGE")
    print("\t./304pacman file")
    print("\tfile\tfile describing the board, using the following characters:\n\t\t    '0' for an empty square,\n\t\t    '1' for a wall,\n\t\t    'F' for the ghost's position,\n\t\t    'P' for Pacman's position.")
    print("DESCRIPTION")
    print("\tMake a pathfinding for pacPan in pygame.")
    return (0)

def check_file(filename):
    fileContent = get_file(filename)
    i = 0
    fCount = 0
    pCount = 0

    while (i < len(fileContent)):
        ii = 0
        while (ii < len(fileContent[i])):
            if (fileContent[i][ii] != '0' and fileContent[i][ii] != '1' and fileContent[i][ii] != 'F' and fileContent[i][ii] != 'P'):
                return (84)
            if (fileContent[i][ii] == 'F'):
                fCount = fCount + 1
            if (fileContent[i][ii] == 'P'):
                pCount = pCount + 1
            ii = ii + 1
        i = i + 1
    if (pCount != 1 or fCount != 1):
        return (84)
    return (0)

def check_error(argv):
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        return (1)
    if (len(argv) != 2):
        print("Error: you need 1 arguments")
        return (84)
    try:
        open(argv[1], "r")
    except:
        print("Error: first argument must be a file")
        return (84)
    if (check_file(argv[1]) == 84):
        print("Error: bad file")
        return (84)
    return (0)
