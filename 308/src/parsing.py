#!/usr/bin/env python3

def print_help():
    print("USAGE")
    print("\t./308reedpipes r0 r5 r10 r15 r20 n")
    print("")
    print("DESCRIPTION")
    print("\tr0\tradius (in cm) of pipe at the 0cm abscissa")
    print("\tr0\tradius (in cm) of pipe at the 5cm abscissa")
    print("\tr0\tradius (in cm) of pipe at the 10cm abscissa")
    print("\tr0\tradius (in cm) of pipe at the 15cm abscissa")
    print("\tr0\tradius (in cm) of pipe at the 20cm abscissa")
    print("\tn\tnumber of points needed to display the radius")
    return (0)

def check_error(argv):
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        return (0)
    if (len(argv) != 7):
        print("Error: too many or too much arguments")
        return (84)
    try:
        float(argv[1])
        float(argv[2])
        float(argv[3])
        float(argv[4])
        float(argv[5])
        int(argv[6])
    except:
        print("Error: all the arguments must be number")
    i = 1
    while (i < 7):
        if (float(argv[i]) <= 0):
            print("Error: all the arguments must ne number > 0")
            return (84)
        i = i + 1
    return (0)
