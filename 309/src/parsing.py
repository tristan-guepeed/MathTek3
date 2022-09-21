#!/usr/bin/env python3

from src.get_file import get_file

def print_help():
    print("USAGE")
    print("\t./309pollution n file x y")
    print("DESCRIPTION")
    print("\tn\tnumber of points on the grid axis")
    print("\tfile\tcsc file containing the data points x;y;p")
    print("\tx\tabscissa of the point whose pollution level we want to know")
    print("\ty\tordinate of the point whose pollution level we want to know")
    return (0)

def check_file(fileName):
    fileContent = get_file(fileName)
    i = 0

    while (i < len(fileContent)):
        ii = 0
        count = 0
        while (ii < len(fileContent[i])):
            if (fileContent[i][ii] == ';'):
                count = count + 1
            ii = ii + 1
        if (count != 2):
            return (84)
        i = i + 1

    i = 0

    while (i < len(fileContent)):
        ii = 0
        tmpNumber = ""
        while (ii < len(fileContent[i]) and fileContent[i][ii] != ';'):
            tmpNumber = tmpNumber + fileContent[i][ii]
            ii = ii + 1
        try:
            int(tmpNumber)
        except:
            return (84)
        ii = ii + 1
        tmpNumber = ""
        while (ii < len(fileContent[i]) and fileContent[i][ii] != ';'):
            tmpNumber =	tmpNumber + fileContent[i][ii]
            ii = ii + 1
        try:
            int(tmpNumber)
        except:
            return (84)
        ii = ii + 1
        tmpNumber = ""
        while (ii < len(fileContent[i])):
            tmpNumber = tmpNumber + fileContent[i][ii]
            ii = ii + 1
        try:
            int(tmpNumber)
        except:
            return (84)
        i = i + 1
    return (0)

def check_error(argv):
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        return (0)
    if (len(argv) != 5):
        print("Error: too much or too many arguments")
        return (84)
    try:
        int(argv[1])
        float(argv[3])
        float(argv[4])
    except:
        print("Error: first, third and fourth must be number")
        return (84)
    if (int(argv[1]) < 0 or int(argv[3]) < 0 or int(argv[4]) < 0):
        print("Error: first, third and fourth must be number >= 0")
        return (84)
    try:
        open(argv[2], "r")
    except:
        print("Error: second argument must be a file")
    if (check_file(argv[2]) == 84):
        print("Error: bad file")
        return (84)
    return (0)
