# _*_ coding : utf-8 _*_

list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

from copy import deepcopy


def turn90(list):
    if not list:
        return False
    line = []
    lines = []
    while list[0]:
        line.clear()
        for i in list:
            line.append(i.pop())
        lines.append(deepcopy(line))
    return lines


while list:
    [print(i,end=' ') for i in list.pop(0)]
    list = turn90(list)
