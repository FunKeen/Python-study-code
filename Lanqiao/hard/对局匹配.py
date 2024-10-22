# https://www.lanqiao.cn/problems/107/learning/?page=1&first_category_id=1&second_category_id=3
import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

arr = set()

res = 0

mem = [[0 for i in range(n + 1)] for j in range(n + 1)]


def dfs(x, y):
    global res
    mem[x][y]=len(arr)
    print(x, y, len(arr))
    if x >= n:
        res = max(res, len(arr))
        return
    if l[x] - k not in arr or l[x] + k not in arr:
        arr.add(l[x])
        dfs(x + 1, y + 1)
        arr.remove(l[x])
    dfs(x + 1, y)


dfs(0, 0)
print(res)
for row in mem:
    print(row)