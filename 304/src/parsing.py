#!/usr/bin/env python3

def print_help():
    print("USAGE")
    print("\t./304pacman file c1 c2")
    print("\tfile\tfile describing the board, using the following characters:\n\t\t    '0' for an empty square,\n\t\t    '1' for a wall,\n\t\t    'F' for the ghost's position,\n\t\t    'P' for Pacman's position.")
    print("\tc1\tcharacter to display for a wall")
    print("\tc2\tcharacter to display for an empty space.")
    print("DESCRIPTION")
    print("\tMake a pacman game.")
    return (0)

def check_error(argv):
    print_help()
    return (0)
