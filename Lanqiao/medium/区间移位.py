# https://www.lanqiao.cn/problems/111/learning/?page=2&first_category_id=1
import sys
from copy import deepcopy

# data = sys.stdin.read().splitlines()
# data = '2\n10 5010\n4980 9980'.splitlines()
# data = '4\n0 4000\n3000 5000\n5001 8000\n7000 10000'.splitlines()
data = '5\n0 2000\n2000 8000\n4000 6000\n8000 10000\n8000 10000'.splitlines()
n = int(data[0])
queue = []
for i in range(1, n + 1):
    a, b = map(int, data[i].split())
    queue.append([a, b])

queue.sort(key=lambda x: x[0] + x[1])

Map = [0] * (n + 1)
Map[0] = queue[0][0]
for i in range(n - 1):
    Map[i + 1] = queue[i + 1][0] - queue[i][1]
Map[-1] = 10000 - queue[-1][1]


def isnot(mid):
    temp_map = deepcopy(Map)
    for i in range(n + 1):
        if i < n:
            x_move = 0
            if temp_map[i] == 0:
                continue
            elif temp_map[i] < 0:
                x_move = max(temp_map[i], -mid)
            elif temp_map[i] > 0:
                x_move = min(temp_map[i], mid)
            temp_map[i + 1] += x_move
            temp_map[i] -= x_move
        if temp_map[i] > 0:
            return False
    return True


def erf(mid):
    l, r = 0, 10 ** 4
    while r - l > 1e-7:
        mid = (l + r) / 2
        if isnot(mid):
            r = mid
        else:
            l = mid
    res = int((mid + 0.05) * 10) / 10
    if res.is_integer():
        print(int(res))
    else:
        print(res)


erf(0)
