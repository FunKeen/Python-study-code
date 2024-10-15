# _*_ coding : utf-8 _*_
n, m = map(int, input().split())
dict = {}
for i in range(1, n + 1):
    dict[i] = {}
for i in range(m):
    u, v, val = map(int, input().split())
    dict[u][v] = val
    dict[v][u] = val

key = [99999999] * (n + 1)
parent = [-1] * (n + 1)


def fun(start):
    S = [start]
    V = [start, 0]
    for x in S:
        pass


fun(1)

print(min(dict[1].values()).__dict__)
