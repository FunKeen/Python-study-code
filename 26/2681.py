# _*_ coding : utf-8 _*_
from math import sqrt, ceil
import sys


class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.maxrank = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                self.rank[y] += 1
                self.maxrank += self.rank[y]


def kruskal(n):
    uf = UnionFind(n)
    res = 0
    mts = []
    for u, v, value in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mts.append(value)
            res = max(res, value)
        if len(mts) == n - 1:
            return res


m = int(input())
ms = list(map(int, input().split()))

n = int(input())
edges = []
point = []
for _ in range(n):
    point.append(list(map(int, input().split())))


def dist(point1, point2):
    return ceil(sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2))


for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, dist(point[i], point[j])])

edges = sorted(edges, key=lambda x: x[2])

yes = kruskal(n)

count = 0
for i in ms:
    if i >= yes:
        count += 1
print(count)
