import sys
from re import findall


class File(object):
    def __init__(self, val, p=None):
        self.val = val
        self.p = p


data = sys.stdin.read().splitlines()
n = int(data[0])
for_len = list(range(1, n + 1))
file = {}


def C(path, size):
    c = findall(r"/\d+|/\w+", path)
    for x in c:
        if x not in file:
            file[x] = {}
        elif file[x]:
            pass
    pass


def R(str):
    print(str)
    pass


def Q(path):
    print(str)
    pass


# 1 文件
for i in for_len:
    c = data[i].split()
    if c[0] == "C":
        C(c[1], c[2])
    elif c[0] == "R":
        R(c[1])
    elif c[0] == "Q":
        Q(c[1:])
