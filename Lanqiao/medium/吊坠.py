# https://www.lanqiao.cn/problems/19719/learning/?page=43&first_category_id=1&second_category_id=3
import sys
from collections import defaultdict
from heapq import heappop, heappush

# data = sys.stdin.read().splitlines()
data = ['5 5', 'eabbb', 'addce', 'ceddc', 'acbbb', 'eccad']
n, m = map(int, data[0].split())
string = data[1:n + 1]


def fun(str1, str2):
    res = 0
    for l in range(m):
        for k in range(m):
            temp1 = str1[l:] + str1[:l]
            temp2 = str2[k:] + str2[:k]
            dp = [[0] * (m + 1) for _ in range(m + 1)]
            for i in range(m):
                for j in range(m):
                    if temp1[i] == temp2[j]:
                        dp[i + 1][j + 1] = dp[i][j] + 1
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            res = max(res, dp[m][m])
    return res


dfdict = defaultdict(dict)

for i in range(n):
    for j in range(i + 1, n):
        val = fun(string[i], string[j])
        dfdict[i][j] = val
        dfdict[j][i] = val


def mts():
    res = 0
    queue = []
    visited = set()
    visited.add(0)
    for end, val in dfdict[0].items():
        heappush(queue, (-val, end))
    while len(visited) < n:
        t_val, t_end = heappop(queue)
        if t_end in visited:
            continue
        visited.add(t_end)
        res -= t_val
        for end, val in dfdict[t_end].items():
            if end not in visited:
                heappush(queue, (-val, end))
    return res


print(mts())
