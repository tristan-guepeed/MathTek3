#!/usr/bin/env python3

from src.draw_paths import draw_paths
from src.get_names import get_names
from src.get_file import get_file
from src.get_degree import get_degree

def print_help():
    print("USAGE")
    print("\t./302separation file [n | p1 p2]")
    print("DESCRIPTION")
    print("\tfile\tfile that contains the list of Facebook connections")
    print("\tn\tmaximum length of the paths")
    print("\tpi\tname of someone in the file")
    return (0)

def check_file(filename):
    fileContent = get_file(filename)
    i = 0

    while (i < len(fileContent)):
        try:
            fileContent[i].index(" is friends with ")
        except:
            return (84)
        if (fileContent[i].index(" is friends with ") == 0):
            return (84)
        if (fileContent[i].index(" is friends with ") + 17 == len(fileContent[i])):
            return (84)
        i = i + 1
    
    return (0)

def check_names(fileContent, name):
    nameContent = get_names(fileContent)
    i = 0

    while (i < len(nameContent)):
        if (name == nameContent[i]):
            return (0)
        i = i + 1
    return (84)

def check_error(argv):
    if (len(argv) < 3 or len(argv) > 4):
        print("Error: too much or too few arguments")
        return (84)
    try:
        open(argv[1], "r")
    except:
        print("Error: first argument must be a file")
        return (84)
    if (check_file(argv[1]) == 84):
        print("Error: bad file")
        return (84)
    if (len(argv) == 3):
        try:
            int(argv[2])
        except:
            print("Error: with 2 arguments, the second must be a number > 0")
            return (84)
        if (int(argv[2]) <= 0):
            print("Error: with 2 arguments, the second must be a number > 0")
        draw_paths(argv)
    if (len(argv) == 4):
        fileContent = get_file(argv[1])
        nameContent = get_names(fileContent)
        if (check_names(fileContent, argv[2]) == 84 or check_names(fileContent, argv[3]) == 84):
            print("Degree of separation between %s and %s: -1" % (argv[2], argv[3]))
            return (0)
        if (argv[2] == argv[3]):
            print("Degree of separation between %s and %s: 0" % (argv[2], argv[3]))
            return (0)
        print("Degree of separation between %s and %s: %d" % (argv[2], argv[3], get_degree(argv[2], argv[3], fileContent, nameContent)))
    return (0)
