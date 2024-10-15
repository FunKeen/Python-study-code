class Unionfind(object):
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)
        if u != v:
            if self.rank[u] > self.rank[v]:
                self.p[v] = u
            elif self.rank[u] < self.rank[v]:
                self.p[u] = v
            else:
                self.p[v] = u
                self.rank[u] += 1


import sys

data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
edges = [list(map(int, x.split())) for x in data[1:]]
edges.sort(key=lambda x: x[2])


def K(n):
    unionfind = Unionfind(n)
    for x, y, val in edges:
        unionfind.union(x, y)
        if unionfind.find(1) == unionfind.find(n):
            sys.stdout.write(f"{val}")
            return


K(n)
