#!/usr/bin/env python3

def init_task(data):
    i = 0
    zob = []
    task_id = []
    while (i != len(data)):
        zob.append(data[i][0].split(";"))
        i+=1
    i = 0
    while (i != len(zob)):
        task_id.append(zob[i][0])
        task_id.append("false")
        i+=1
    return task_id

def init_duration(data):
    i = 0
    zob = []
    task_duration = []
    while (i != len(data)):
        zob.append(data[i][0].split(";"))
        i+=1
    i = 0
    while (i != len(zob)):
        task_duration.append(zob[i][0])
        task_duration.append(zob[i][2])
        i+=1
    return task_duration

def init_required(data):
    i = 0
    zob = []
    task_required = []
    while (i != len(data)):
        zob.append(data[i][0].split(";"))
        i+=1
    i, j = 0, 3
    while (i != len(zob)):
        task_required.append(zob[i][0])
        while (j != len(zob[i])):
            task_required.append(zob[i][j])
            j+=1
        task_required.append("/")
        j = 3
        i+=1
    return task_required

def construction(data):
    task_id = init_task(data)
    task_duration = init_duration(data)
    task_required = init_required(data)
    t = 0
    return 0