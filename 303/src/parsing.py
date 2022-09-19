#!/usr/bin/env python3

def print_help():
    print("USAGE")
    print("\t./303make makefile [file]")
    print("DESCRIPTION")
    print("\tmakefile\tname of the makefile")
    print("\tfile\t\tname of a recently modified file")
    return (0)

def check_errors(argv):
    if (len(argv) < 2 or len(argv) > 3):
        print("Need 2 or 3 arguments")
        return 84
    if (len(argv) == 2 and argv[1] == '-h'):
        print_help()
        return 1
    if (len(argv) == 2):
        return 2
    if (len(argv) == 3):
        return 3
    return 0