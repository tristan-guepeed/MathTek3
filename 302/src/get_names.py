#!/usr/bin/env python3

def get_first_name(line):
    name = ""
    i = 0

    while (i < line.index(" is friends with ")):
        name = name + line[i]
        i = i + 1
    return (name)

def get_last_name(line):
    name = ""
    i = line.index(" is friends with ") + 17

    while (i < len(line)):
        name = name + line[i]
        i = i + 1
    return (name)

def check_double(tmp, nameContent):
    i = 0

    while (i < len(nameContent)):
        if (nameContent[i] == tmp):
            return (0)
        i = i + 1
    return (-1)

def get_names(fileContent):
    i = 0
    nameContent = []

    while (i < len(fileContent)):
        tmp = get_first_name(fileContent[i])
        if (check_double(tmp, nameContent) == -1):
            nameContent.append(tmp)
        tmp = get_last_name(fileContent[i])
        if (check_double(tmp, nameContent) == -1):
            nameContent.append(tmp)
        i = i + 1
    nameContent.sort()
    return (nameContent)
