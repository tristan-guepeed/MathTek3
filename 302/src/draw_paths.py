#!/usr/bin/env python3

from src.get_file import get_file
from src.get_names import get_names
from src.get_degree import get_degree
from src.get_degree import check_link

def draw_paths(argv):
    fileContent = get_file(argv[1])
    nameContent = get_names(fileContent)
    i = 0

    while (i < len(nameContent)):
        print(nameContent[i])
        i = i + 1
    print("")
    i = 0
    while (i < len(nameContent)):
        ii = 0
        while (ii < len(nameContent)):
            if (i == ii):
                print("0", end='')
            elif (i != ii):
                print("%d" % check_link(nameContent[i], nameContent[ii], fileContent), end='')
            if (ii + 1 < len(nameContent)):
                print(" ", end='')
            ii = ii + 1
        print("")
        i = i + 1
    print("")


    i = 0
    while (i < len(nameContent)):
        ii = 0
        while (ii < len(nameContent)):
            if (i == ii):
                print("0", end='')
            elif (i != ii):
                if (check_link(nameContent[i], nameContent[ii], fileContent) == 1):
                    print("1", end='')
                elif (check_link(nameContent[i], nameContent[ii], fileContent) != 1):
                    if (get_degree(nameContent[i], nameContent[ii], fileContent, nameContent) > int(argv[2])):
                        print("0", end='')
                    elif (get_degree(nameContent[i], nameContent[ii], fileContent, nameContent) <= int(argv[2])):
                        print("%d" % get_degree(nameContent[i], nameContent[ii], fileContent, nameContent), end='')
            if (ii + 1 < len(nameContent)):
                print(" ", end='')
            ii = ii + 1
        print("")
        i = i + 1
    return (0)
