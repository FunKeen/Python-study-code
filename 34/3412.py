import sys

data = sys.stdin.read().splitlines()
n, l, r, t = map(int, data[0].split())
mem = []
for i in range(1, n + 1):
    mem.append(list(map(int, data[i].split())))

s = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            s[0][0] = mem[0][0]
        elif i == 0:
            s[i][j] = s[i][j - 1] + mem[i][j]
        elif j == 0:
            s[i][j] = s[i - 1][j] + mem[i][j]
        else:
            s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + mem[i][j]


def getval(x, y):
    if x < 0 or y < 0:
        return 0
    return s[x][y]


count = 0
for i in range(n):
    for j in range(n):
        x1 = i - r
        y1 = j - r
        x2 = i + r
        y2 = j + r
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 >= n:
            x2 = n - 1
        if y2 >= n:
            y2 = n - 1
        if getval(x2, y2) - getval(x2, y1 - 1) - getval(x1 - 1, y2) + getval(x1 - 1, y1 - 1) <= (x2 - x1 + 1) * (
                y2 - y1 + 1) * t:
            count += 1
print(count)
