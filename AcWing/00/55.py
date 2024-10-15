# _*_ coding : utf-8 _*_
# import sys
#
# data = list(map(int, sys.stdin.read().split()))
#

# print(data)


def getsum(i, re=0):
    x = data[i]
    if i == 0:
        re = x
    else:
        temp1 = onesum(i)
        temp = getsum(i - 1)
        re = max(temp, temp1)
    return re


def onesum(i, re=0):
    for x in range(i + 1):
        re = max(sum(data[x:i + 1]), re)
    return re


data = [1, -2, 3, 10, -4, 7, 2, -5]

print(getsum(7))
