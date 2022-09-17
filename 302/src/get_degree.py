#!/usr/bin/env python3

def check_link(first, second, fileContent):
    i = 0

    while (i < len(fileContent)):
        try:
            fileContent[i].index(first)
            fileContent[i].index(second)
            return (1)
        except:
            i = i + 1
    return (0)

def valid(currentName, first, second, namePassed):
    if (currentName == first or currentName == second):
        return (-1)
    i = 0
    while (i < len(namePassed)):
        if (currentName == namePassed[i]):
            return (-1)
        i = i + 1
    return (0)

def check_all_links(first, second, fileContent, nameContent, link, namePassed, limit):
    if (link > limit):
        return (0)
    if (check_link(first, second, fileContent) == 1):
        return (link + 1)
    i = 0
    while (i < len(nameContent)):
        if (valid(nameContent[i], first, second, namePassed) == 0):
            ii = 0
            while (ii < len(fileContent)):
                try:
                    fileContent[ii].index(first)
                    fileContent[ii].index(nameContent[i])
                    namePassed.append(first)
                    tmpRes = check_all_links(nameContent[i], second, fileContent, nameContent, link + 1, namePassed, limit)
                    if (tmpRes != 0):
                        return (tmpRes)
                    namePassed.remove(first)
                    ii = ii + 1
                except:
                    ii = ii + 1
        i = i + 1
    return (0)

def get_degree(first, second, fileContent, nameContent):
    i = 1

    while (i < len(nameContent)):
        namePassed = []
        tmp = check_all_links(first, second, fileContent, nameContent, 0, namePassed, i)
        if (tmp > 0):
            return (tmp)
        i = i + 1
    return (0)
