# https://www.lanqiao.cn/problems/19712/learning/?page=1&first_category_id=1&second_category_id=3&sort=difficulty&asc=1
import sys
from copy import deepcopy

data = sys.stdin.read().splitlines()
n, k = map(int, data[0].split())
Map = []
for i in range(1, n + 1):
    Map.append(list(map(int, data[i].split())))

vsi = [[0 for _ in range(n)] for _ in range(n)]

cx = [-1, -1, 0, 1, 1, 1, 0, -1]
cy = [0, 1, 1, 1, 0, -1, -1, -1]

rsize = n - 1
Msize = n ** 2 - 2

next = [i for i in range(1, k)] + [0]

res = []

xdirt = (1, 3, 5, 7)


#
# def dfs(x, y, goes):
#     q = [(x, y, goes, vsi)]
#     vsi[x][y] = 1
#     while q:
#         tx, ty, t_goes, t_vsi = q.pop()
#         for i in range(7, -1, -1):
#             dx = tx + cx[i]
#             dy = ty + cy[i]
#             if 0 <= dx < n and 0 <= dy < n:
#                 if t_vsi[dx][dy] == 1:
#                     continue
#                 if next[Map[tx][ty]] != Map[dx][dy]:
#                     continue
#                 if i in xdirt and t_vsi[tx][dy] == 1 and t_vsi[dx][ty] == 1:
#                     continue
#                 if dx == rsize and dy == rsize:
#                     if len(t_goes) == Msize:
#                         print(t_goes + str(i))
#                         return
#                     continue
#                 t_vsi[dx][dy] = 1
#                 q.append((dx, dy, t_goes + str(i), deepcopy(t_vsi)))
#                 t_vsi[dx][dy] = 0
#     print(-1)


def dfs(tx, ty, t_goes, t_vsi):
    vsi[tx][ty] = 1
    for i in range(8):
        dx = tx + cx[i]
        dy = ty + cy[i]
        if 0 <= dx < n and 0 <= dy < n:
            if t_vsi[dx][dy] == 1:
                continue
            if next[Map[tx][ty]] != Map[dx][dy]:
                continue
            if i in xdirt and t_vsi[tx][dy] == 1 and t_vsi[dx][ty] == 1:
                continue
            if dx == rsize and dy == rsize:
                if len(t_goes) == Msize:
                    print(t_goes + str(i))
                    sys.exit()
                continue
            t_vsi[dx][dy] = 1
            dfs(dx, dy, t_goes + str(i), t_vsi)
            t_vsi[dx][dy] = 0


dfs(0, 0, '', vsi)
print(-1)
