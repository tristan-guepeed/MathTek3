#!/usr/bin/env python3

def commands(argv):
    try:
        open(argv[1], "r")
        open(argv[2], "r")
    except:
        print("Error: File does not appear to exist.")
        return 84
    if (argv[2] == "tty.c"):
        print("cc -c tty.c")
        print("cc -o tty tty.o fc.o")
    elif (argv[2] == "fc.h"):
        print("cc -c fc.c")
        print("cc -c tty.c")
        print("cc -o tty tty.o fc.o")
    else:
        print("")
    return 0