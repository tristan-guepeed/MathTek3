#!/usr/bin/env python3

def print_help():
    print("USAGE")
    print("\t./301dannon file")
    print("DESCRIPTION")
    print("\tfile\tfile that contains the numbers to be sorted, separated by spaces")
    return (0)

def check_error(argv):
    if (len(argv) != 2):
        print("Need one argument")
        return 84
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        return 1
    numbers = []
    i = 0
    try:
        fileData = open(argv[1], "r")
        for l in fileData:
            data=[str(d) for d in l.split(" ")]
            while(len(data) > i):
                num =float(data[i])
                numbers.append(num)
                i = i + 1
        return (numbers)
    except:
        print("Error: File does not appear to exist.")
        return 84
