class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[y] > self.rank[x]:
                self.parent[x] = y
            elif self.rank[x] == self.rank[y]:
                self.parent[y] = x
                self.rank[x] += 1
