#!/usr/bin/env python3

def print_help():
    print("USAGE")
    print("\t./307multigrains n1 n2 n3 n4 po pw pc pb ps")
    print("")
    print("DESCRIPTION")
    print("\tn1\tnumber of tons of fertilizer F1")
    print("\tn2\tnumber of tons of fertilizer F2")
    print("\tn3\tnumber of tons of fertilizer F3")
    print("\tn4\tnumber of tons of fertilizer F4")
    print("\tpo\tpriceof one unit of oat")
    print("\tpw\tpriceof one unit of wheat")
    print("\tpc\tpriceof one unit of corn")
    print("\tpb\tpriceof one unit of barley")
    print("\tps\tpriceof one unit of soy")
    return (0)

def check_errors(argv):
    if len(argv) != 10:
        print("Need 10 arguments")
        exit(84)
    i = 0
    while (i != len(argv)):
        try:
            if (not int(argv[i])):
                pass
        except:
            print("Number excepted")
            exit(84)
        if (int(argv[i]) < 0):
            print("Positive value expected")
            exit(84)
    return 0