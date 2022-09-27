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

def take_first_task(task_required):
    i = 1
    first_task = []

    while (i != len(task_required) - 1):
        if (task_required[i + 1] == "/" and task_required[i - 1] == "/"):
            first_task.append(task_required[i])
        i+=1
    return first_task

def activate_task(task_id, task):
    i = 0

    while(i != len(task_id)):
        if (task_id[i] == task):
            task_id[i + 1] = "true"
        i+=1
    return task_id

def check_others_task(task_order, task_required, task_duration, task_id):


    return task_order

def construction(data):
    task_id = init_task(data)
    task_duration = init_duration(data)
    task_required = init_required(data)
    task_required.insert(0, "/")
    task_order = take_first_task(task_required)
    task_id = activate_task(task_id, task_order[0])

    if (len(task_order) == 1):
        check_others_task(task_order, task_required, task_duration, task_id)
        return 0
    else:
        #si y'a plusieurs premières task
        return 0
    return 0