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
    print_help()
    return (0)
