# https://www.lanqiao.cn/problems/19726/learning/?page=1&first_category_id=1
import sys
from collections import defaultdict

data = sys.stdin.read().splitlines()
n, m, Qn = map(int, data[0].split())

qdict = defaultdict(list)
Q = []

for i in range(1, m + 1):
    a, b = map(int, data[i].split())
    qdict[a].append(b)
    qdict[b].append(a)

for i in range(m + 1, m + Qn + 1):
    Q.append(tuple(map(int, data[i].split())))


def bfs(start, times):
    vis = set()
    q = [(start, times)]
    vis.add(start)

    while q:
        s, t = q.pop(0)
        if t > 0:
            for next in qdict[s]:
                if next not in vis:
                    vis.add(next)
                    q.append((next, t - 1))
    return len(vis)


count = 0
for be, ed in Q:
    count += bfs(be, ed)

print(f"{count / Qn:.2f}")
