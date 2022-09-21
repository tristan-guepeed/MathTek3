#!/usr/bin/env python3

import pygame
from src.get_file import get_file

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

def draw_help(fenetre):
    font = pygame.font.SysFont(None, 50)
    fenetre.blit(font.render(": Wall", True, [0, 0, 0]), (110, 58))
    pygame.draw.rect(fenetre, [255, 0, 0], [50, 50, 50, 50])
    fenetre.blit(font.render(": Empty Space", True, [0, 0, 0]), (110, 158))
    pygame.draw.rect(fenetre, [0, 255, 0], [50, 150, 50, 50])
    fenetre.blit(font.render(": Pacman", True, [0, 0, 0]), (110, 258))
    pygame.draw.rect(fenetre, [0, 0, 0], [50, 250, 50, 50])
    fenetre.blit(font.render(": Ghost", True, [0, 0, 0]), (110, 358))
    pygame.draw.rect(fenetre, [255, 255, 255], [50, 350, 50, 50])
    fenetre.blit(font.render(": All paths", True, [0, 0, 0]), (110, 458))
    pygame.draw.rect(fenetre, [0, 0, 255], [50, 450, 50, 50])
    fenetre.blit(font.render(": Good path", True, [0, 0, 0]), (110, 558))
    pygame.draw.rect(fenetre, [255, 255, 0], [50, 550, 50, 50])
    return (0)

def draw_map(pacMap, fenetre):
    i = 0
    x = 400
    y = 50
    while (i < len(pacMap)):
        ii = 0
        x = 400
        while (ii < len(pacMap[i])):
            if (pacMap[i][ii] == 'o'):
                pygame.draw.rect(fenetre, [255, 0, 0], [x, y, 50, 50])
            elif (pacMap[i][ii] == ' '):
                pygame.draw.rect(fenetre, [0, 255, 0], [x, y, 50, 50])
            elif (pacMap[i][ii] == 'P'):
                pygame.draw.rect(fenetre, [0, 0, 0], [x, y, 50, 50])
            elif (pacMap[i][ii] == 'F'):
                pygame.draw.rect(fenetre, [255, 255, 255], [x, y, 50, 50])
            else:
                pygame.draw.rect(fenetre, [0, 0, 255], [x, y, 50, 50])
            x = x + 50
            ii = ii + 1
        y = y + 50
        i = i + 1
    return (0)

def draw_good_path(pacMap, count, fenetre):
    x = 0
    y = 0
    while (pacMap[x][y] != 'P'):
        x = x + 1
        if (x >= len(pacMap)):
            x = 0
            y = y + 1
    while (count > 0):
        if (x - 1 >= 0):
            if (pacMap[x - 1][y] == get_char(count % 10)):
                x = x - 1
                pygame.draw.rect(fenetre, [255, 255, 0], [y * 50 + 400, x * 50 + 50, 50, 50])
        if (y + 1 < len(pacMap[x])):
            if (pacMap[x][y + 1] == get_char(count % 10)):
                y = y + 1
                pygame.draw.rect(fenetre, [255, 255, 0], [y * 50 + 400, x * 50 + 50, 50, 50])
        if (x + 1 < len(pacMap)):
            if (pacMap[x + 1][y] == get_char(count % 10)):
                x = x + 1
                pygame.draw.rect(fenetre, [255, 255, 0], [y * 50 + 400, x * 50 + 50, 50, 50])
        if (y - 1 >= 0):
            if (pacMap[x][y - 1] == get_char(count % 10)):
                y = y - 1
                pygame.draw.rect(fenetre, [255, 255, 0], [y * 50 + 400, x * 50 + 50, 50, 50])
        count = count - 1
    return (0)

def find_the_path(pacMap, emptySpace):
    end = 0
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

    pygame.init()
    clock = pygame.time.Clock()
    fenetre = pygame.display.set_mode((1920, 1080))
    loop = True
    background = pygame.Surface(fenetre.get_size())
    while (loop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        background.fill([0, 200, 255])
        fenetre.blit(background, (0, 0))
        draw_map(pacMap, fenetre)
        if (end == 1):
            draw_good_path(pacMap, count - 1, fenetre)
        draw_help(fenetre)
        pygame.display.flip()
        clock.tick(10)
        pygame.event.pump()
        pygame.time.delay(500)
        if (count < 100):
            turn = 1
            while (turn < maxTurn):
                i = x - turn
                ii = y
                while (i < x and end == 0):
                    if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                        if (pacMap[i][ii] == get_char((count - 1) % 10)):
                            pacMap = put_way(pacMap, count, emptySpace, i, ii)
                            if (check_end(pacMap, count, i, ii) == 0):
                                end = 1
                    i = i + 1
                    ii = ii + 1
                i = x
                ii = y + turn
                while (ii > y and end == 0):
                    if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                        if (pacMap[i][ii] == get_char((count - 1) % 10)):
                            pacMap = put_way(pacMap, count, emptySpace, i, ii)
                            if (check_end(pacMap, count, i, ii) == 0):
                                end = 1
                    i = i + 1
                    ii = ii - 1
                ii = y
                i = x + turn
                while (i > x and end == 0):
                    if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                        if (pacMap[i][ii] == get_char((count - 1) % 10)):
                            pacMap = put_way(pacMap, count, emptySpace, i, ii)
                            if (check_end(pacMap, count, i, ii) == 0):
                                end = 1
                    i = i - 1
                    ii = ii - 1
                ii = y - turn
                i = x
                while (ii < y and end == 0):
                    if (i >= 0 and i < len(pacMap) and ii >= 0 and ii < len(pacMap[i])):
                        if (pacMap[i][ii] == get_char((count - 1) % 10)):
                            pacMap = put_way(pacMap, count, emptySpace, i, ii)
                            if (check_end(pacMap, count, i, ii) == 0):
                                end = 1
                    ii = ii + 1
                    i = i - 1
                turn = turn + 1
            if (end == 0):
                count = count + 1
    pygame.quit()
    return (0)

def pathfinding(argv):
    pacMap = get_file(argv[1])
    pacMap = replace_map(pacMap, 'o', ' ')
    pacMap = put_one(pacMap, ' ')
    if (check_one(pacMap) == 0):
        return (0)
    find_the_path(pacMap, ' ')
    return (0)
