# https://www.lanqiao.cn/problems/19704/learning/?page=1&first_category_id=1
import sys
from collections import defaultdict

data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
c = [0] + list(map(int, data[1].split()))
d = [0] + list(map(int, data[2].split()))

dict_c = defaultdict(list)
dict_d = defaultdict(list)
dict_c[0].append(1)
dict_d[0].append(1)

for i in range(3, n + 2):
    a, b = map(int, data[i].split())
    dict_c[a].append(b)
    dict_c[b].append(a)
for i in range(n + 2, n + m + 1):
    a, b = map(int, data[i].split())
    dict_d[a].append(b)
    dict_d[b].append(a)

viewc = set()
viewd = set()
max_step = 0


def dfs(sc, sd, step):
    global max_step
    q = [(sc, sd, step, viewc, viewd)]
    while q:
        tc, td, step, tvc, tvd = q.pop()
        if tc in dict_c and td in dict_d:
            for i in dict_c[tc]:
                for j in dict_d[td]:
                    if i not in tvc and j not in tvd and c[i] == d[j]:
                        tvc.add(i)
                        tvd.add(j)
                        max_step = max(max_step, step + 1)
                        q.append((i, j, step + 1, tvc, tvd))


dfs(0, 0, 0)

print(max_step)
