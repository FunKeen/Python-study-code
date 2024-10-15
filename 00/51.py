# _*_ coding : utf-8 _*_

from re import findall

str = input()
list = list(map(int, findall(r"\d+", str)))
arr = []


def dfs(x):
    if len(arr) == len(list):
        print(arr)
        return
    for i in list:
        arr.append(i)
        dfs(x + 1)
        arr.pop()


st = [0] * len(list)


def dfs2(x):
    if len(arr) == len(list):
        print(arr)
        return
    for i in list:
        if st[list.index(i)] == 0:
            st[list.index(i)] = 1
            arr.append(i)
            dfs2(x + 1)
            arr.pop()
            st[list.index(i)] = 0


dfs2(0)
