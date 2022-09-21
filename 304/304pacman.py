#!/usr/bin/env python3

from sys import argv, exit
from src.parsing import check_error
from src.pathfinding import pathfinding

def main():
    rt = check_error(argv)
    if (rt == 84):
        return (84)
    elif (rt == 1):
        return (0)
    pathfinding(argv)
    return (0)

if __name__ == "__main__":
    exit(main())
