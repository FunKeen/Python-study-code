# _*_ coding : utf-8 _*_


# UnionFind类，检查两个点是否已在生成树中、是否连接，添加新的连接
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
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y


# kruskal算法，每次根据最小权值添加一条边，添加完后再检查节点1与节点n是否连接，如果连接的话，直接返回新添加边的权值，该值即为结果
def kruskal(n, edges):
    uf = UnionFind(n)
    mts=[]
    for u, v, val in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mts.append([u, v, val])
        if uf.find(1) == uf.find(n):
            return val


# 输入值
n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

# 给边按照权值升序
edges = sorted(edges, key=lambda x: x[2])
# 输出算法运行结果
print(kruskal(n, edges))
