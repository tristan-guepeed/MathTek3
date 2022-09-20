#!/usr/bin/env python3

import csv

def print_help():
    print("USAGE")
    print("\t./305construction file")
    print("")
    print("DESCRIPTION")
    print("\tfile\tfile describing the tasks")
    return (0)

def check_errors(argv):
    if (len(argv) != 2):
        print("Need two arguments")
        return 84
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        return 1
    try:
        rows = []
        with open(argv[1], 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
    except:
        print("Error: File does not appear to exist.")
        return 84
    return(rows)