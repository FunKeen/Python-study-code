# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().split()
index = 0

r, c, k = map(int, data[index:index + 3])
index += 3

house = []
for _ in range(r):
    house.append(list(map(int, data[index:index + c])))
    index += c

jump = []
for _ in range(r):
    jump.append([0] * c)

mem = []
for _ in range(r):
    mem.append([0] * c)


def fun(x, y):
    global res, mem
    if mem[x][y]:
        jump[0][0] += mem[x][y]
        return
    jump[r - 1][c - 1] = 0
    for i in range(x + 1, r - 1):
        for j in range(y + 1, c - 1):
            if house[i][j] != house[x][y]:
                jump[i][j] += + 1
                jump[0][0] += 1
                print(i,j)
                fun(i, j)
    mem[x][y] = jump[r - 1][c - 1]


fun(0, 0)
print(jump[0][0])
