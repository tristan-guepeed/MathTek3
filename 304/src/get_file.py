#!/usr/bin/env python3

def get_file(filename):
    fileContent = []
    file = open(filename, "r")
    lines = file.readlines()

    for line in lines:
        fileContent.append(line.strip())
    file.close()
    return (fileContent)
