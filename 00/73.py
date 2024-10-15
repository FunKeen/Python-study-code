# _*_ coding : utf-8 _*_
from re import findall

str = "[1,2,3,3,4,4]"
list = list(map(int, findall(r"\d+", str)))
res = {}
for i in list:
    try:
        res[i] += 1
    except KeyError:
        res[i] = 1
for i in res.items():
    if i[1] == 1:
        print(i[0])
