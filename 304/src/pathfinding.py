#!/usr/bin/env python3

from src.get_file import get_file

def draw_map(pacMap):
    i = 0

    while (i < len(pacMap)):
        ii = 0
        while (ii < len(pacMap[i])):
            print(pacMap[i][ii], end='')
            ii = ii + 1
        print("")
        i = i + 1
    return (0)

def replace_map(pacMap, wall, emptySpace):
    i = 0
    newPacMap = []

    while (i < len(pacMap)):
        ii = 0
        tmp = []
        while (ii < len(pacMap[i])):
            if (pacMap[i][ii] != '1' and pacMap[i][ii] != '0'):
                tmp.append(pacMap[i][ii])
            elif (pacMap[i][ii] == '1'):
                tmp.append(wall[0])
            elif (pacMap[i][ii] == '0'):
                tmp.append(emptySpace[0])
            ii = ii + 1
        newPacMap.append(tmp)
        i = i + 1
    return (newPacMap)

def put_one(pacMap, emptySpace):
    i = 0
    ii = 0
    end = 0

    while (pacMap[i][ii] != 'F'):
        i = i + 1
        if (i >= len(pacMap)):
            i = 0
            ii = ii + 1
    if (i - 1 >= 0):
        if (pacMap[i - 1][ii] == emptySpace):
            pacMap[i - 1][ii] = '1'
        elif (pacMap[i - 1][ii] == 'P'):
            end = 1
    if (ii + 1 < len(pacMap[i]) and end == 0):
        if (pacMap[i][ii + 1] == emptySpace):
            pacMap[i][ii + 1] = '1'
        elif (pacMap[i][ii + 1] == 'P'):
            end = 1
    if (i + 1 < len(pacMap) and end == 0):
        if (pacMap[i + 1][ii] == emptySpace):
            pacMap[i + 1][ii] = '1'
        elif (pacMap[i + 1][ii] == 'P'):
            end = 1
    if (ii - 1 >= 0 and end == 0):
        if (pacMap[i][ii - 1] == emptySpace):
            pacMap[i][ii - 1] =	'1'
        elif (pacMap[i][ii - 1] == 'P'):
            end = 1
    return (pacMap)

def check_one(pacMap):
    i = 0
    ii = 0

    while (pacMap[i][ii] != 'F'):
        i = i + 1
        if (i >= len(pacMap)):
            i = 0
            ii = ii + 1
    if (i - 1 >= 0):
        if (pacMap[i - 1][ii] == 'P'):
            return (0)
    if (ii + 1 < len(pacMap[i])):
        if (pacMap[i][ii + 1] == 'P'):
            return (0)
    if (i + 1 < len(pacMap)):
        if (pacMap[i + 1][ii] == 'P'):
            return (0)
    if (ii - 1 >= 0):
        if (pacMap[i][ii - 1] == 'P'):
            return (0)
    return (-1)

def get_char(nb):
    if (nb == 0):
        return ('0')
    elif (nb == 1):
        return ('1')
    elif (nb == 2):
        return ('2')
    elif (nb == 3):
        return ('3')
    elif (nb == 4):
        return ('4')
    elif (nb == 5):
        return ('5')
    elif (nb == 6):
        return ('6')
    elif (nb == 7):
        return ('7')
    elif (nb == 8):
        return ('8')
    elif (nb == 9):
        return ('9')

def put_way(pacMap, count, emptySpace, i, ii):
    end = 0

    if (i - 1 >= 0):
        if (pacMap[i - 1][ii] == emptySpace):
            pacMap[i - 1][ii] = get_char((count) % 10)
        elif (pacMap[i - 1][ii] == 'P'):
            end = 1
    if (ii + 1 < len(pacMap[i]) and end == 0):
        if (pacMap[i][ii + 1] == emptySpace):
            pacMap[i][ii + 1] = get_char((count) % 10)
        elif (pacMap[i][ii + 1] == 'P'):
            end = 1
    if (i + 1 < len(pacMap) and end == 0):
        if (pacMap[i + 1][ii] == emptySpace):
            pacMap[i + 1][ii] = get_char((count) % 10)
        elif (pacMap[i + 1][ii] == 'P'):
            end = 1
    if (ii - 1 >= 0 and end == 0):
        if (pacMap[i][ii - 1] == emptySpace):
            pacMap[i][ii - 1] = get_char((count) % 10)
        elif (pacMap[i][ii - 1] == 'P'):
            end = 1
    return (pacMap)

def check_end(pacMap, count, i, ii):
    if (i - 1 >= 0):
        if (pacMap[i - 1][ii] == 'P'):
            return (0)
    if (ii + 1 < len(pacMap[i])):
        if (pacMap[i][ii + 1] == 'P'):
            return (0)
    if (i + 1 < len(pacMap)):
        if (pacMap[i + 1][ii] == 'P'):
            return (0)
    if (ii - 1 >= 0):
        if (pacMap[i][ii - 1] == 'P'):
            return (0)
    return (-1)

def find_the_path(pacMap, emptySpace):
    maxTurn = 0
    if (len(pacMap) > len(pacMap[0])):
        maxTurn = len(pacMap)
    elif (len(pacMap) <= len(pacMap[0])):
        maxTurn = len(pacMap[0])
    count = 2
    x = 0
    y = 0

    while (pacMap[x][y] != 'F'):
        x = x + 1
        if (x >= len(pacMap)):
            x = 0
            y = y + 1
    while (count < 100):
        turn = 1
        while (turn < maxTurn):
            i = x - turn
            ii = y
            while (i < x):
                if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                    if (pacMap[i][ii] == get_char((count - 1) % 10)):
                        pacMap = put_way(pacMap, count, emptySpace, i, ii)
                        if (check_end(pacMap, count, i, ii) == 0):
                            draw_map(pacMap)
                            return (0)
                i = i + 1
                ii = ii + 1


            i = x
            ii = y + turn
            while (ii > y):
                if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                    if (pacMap[i][ii] == get_char((count - 1) % 10)):
                        pacMap = put_way(pacMap, count, emptySpace, i, ii)
                        if (check_end(pacMap, count, i, ii) == 0):
                            draw_map(pacMap)
                            return (0)
                i = i + 1
                ii = ii - 1

        
            
            ii = y
            i = x + turn
            while (i > x):
                if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                    if (pacMap[i][ii] == get_char((count - 1) % 10)):
                        pacMap = put_way(pacMap, count, emptySpace, i, ii)
                        if (check_end(pacMap, count, i, ii) == 0):
                            draw_map(pacMap)
                            return (0)
                i = i - 1
                ii = ii - 1


            ii = y - turn
            i = x
            while (ii < y):
                if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                    if (pacMap[i][ii] == get_char((count - 1) % 10)):
                        pacMap = put_way(pacMap, count, emptySpace, i, ii)
                        if (check_end(pacMap, count, i, ii) == 0):
                            draw_map(pacMap)
                            return (0)
                ii = ii + 1
                i = i - 1

            turn = turn + 1
        

        count = count + 1
    print("No path found")
    return (0)

def pathfinding(argv):
    pacMap = get_file(argv[1])
    pacMap = replace_map(pacMap, argv[2], argv[3])
    pacMap = put_one(pacMap, argv[3])
    if (check_one(pacMap) == 0):
        draw_map(pacMap)
        return (0)
    find_the_path(pacMap, argv[3])
    return (0)
