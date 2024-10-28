# https://www.lanqiao.cn/problems/653/learning/?page=7
import sys
from collections import defaultdict

lst = []

for i in range(10 ** 5):
    dict = defaultdict(int)
    temp = i ** 2
    for t in str(temp):
        dict[t] += 1
    if all(t == 1 for t in dict.values()):
        lst.append(temp)
    else:
        continue

d = set()
count = 0


def dfs(string, size):
    global count
    leng = len(string)
    if leng > 10:
        return
    if leng == 10:
        dict = {str(x): 0 for x in range(10)}
        for i in string:
            dict[i] += 1
        if all(i == 1 for i in dict.values()):
            count += 1
            print(count)
        return
    for i in range(size, len(lst)):
        if lst[i] not in d:
            d.add(lst[i])
            temp = string
            temp += str(lst[i])
            dfs(temp, i + 1)
            d.remove(lst[i])


dfs('', 0)
