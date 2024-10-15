# _*_ coding : utf-8 _*_
from re import findall

s = input()
w = list(map(int, findall(r'\d+', s)))


def fun():
    if not w:
        return 0
    max = w[0]
    min = w[0]
    for i in w:
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min


print(fun())
