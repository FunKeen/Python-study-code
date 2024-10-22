# https://www.lanqiao.cn/problems/125/learning/?page=2&first_category_id=1&second_category_id=3
import sys
from copy import deepcopy

# Map = []
# for i in range(2):
#     Map.append(list(input()))
Map = [['*', ' ', 'A'], ['*', '*', 'B']]
cx = [1, 0, -1, 0]
cy = [0, 1, 0, -1]

end = deepcopy(Map)

for i in range(2):
    for j in range(3):
        if Map[i][j] == 'A':
            endb = (i, j)
        elif Map[i][j] == 'B':
            enda = (i, j)
        elif Map[i][j] == ' ':
            blank = (i, j)


def bfs(x):
    goes = set()
    goes.add(tuple(tuple(row) for row in Map))
    q = [(x, Map, blank)]
    while q:
        step, temp_map, temp_blank = q.pop(0)
        x, y = temp_blank
        for i in range(4):
            dx = x + cx[i]
            dy = y + cy[i]
            if 0 <= dx < 2 and 0 <= dy < 3:
                temp_map[x][y], temp_map[dx][dy] = temp_map[dx][dy], temp_map[x][y]
                tuple_map = tuple(tuple(row) for row in temp_map)
                if tuple_map in goes:
                    temp_map[x][y], temp_map[dx][dy] = temp_map[dx][dy], temp_map[x][y]
                    continue
                if temp_map[enda[0]][enda[1]] == 'A' and temp_map[endb[0]][endb[1]] == 'B':
                    print(step)
                    sys.exit()
                goes.add(tuple_map)
                q.append((step + 1, deepcopy(temp_map), (dx, dy)))
                temp_map[x][y], temp_map[dx][dy] = temp_map[dx][dy], temp_map[x][y]


bfs(1)
