# https://www.lanqiao.cn/problems/19684/learning/?page=1&first_category_id=1
import sys

n = int(input())

arr = []
st = [0] * (n + 1)


def dfs(x):
    if x >= n:
        print(*arr)
    for i in range(1, n + 1):
        if st[i] == 0:
            st[i] = 1
            arr.append(i)
            dfs(x + 1)
            arr.pop()
            st[i] = 0


dfs(0)
